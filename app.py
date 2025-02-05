import os
from wcwidth import wcswidth
import sys
import uuid
import json
from datetime import datetime
from groq import Groq, DefaultHttpxClient
from dotenv import load_dotenv
from markdown import append_file, render_single_line, set_thinking, screen_columns

# Load environment variables from .env file
load_dotenv()

# Proxy setting
#http_proxy = "http://127.0.0.1:7897"
http_proxy = None

client = Groq(http_client=DefaultHttpxClient(proxy=http_proxy))

# Begin history conversation
# python app.py <conversation_id>

############################################################################

def log_interaction(log_filename, append):
    try:
        with open(log_filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []  # Initialize as an empty list if the file doesn't exist or is empty

    data.insert(0, append)

    with open(log_filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_conversation(conversation_id: str):
    if not conversation_id.isalnum() or len(conversation_id) != 8:
        print("Invalid conversation ID.\n")
        exit(1)
    files = os.listdir('logs')
    files = [f for f in files if f.endswith('.json')]
    files = [f for f in files if conversation_id in f]
    if len(files) != 1:
        print("Conversation not found.\n")
        exit(1)
    filename = files[0]
    try:
        with open(f'logs/{filename}', 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data[0]
    except Exception as e:
        print(f"Failed to load conversation: {str(e)}\n")
        return None


def output_with_ration(text, ratio):
    if wcswidth(text) <= screen_columns() * ratio:
        return text
    length = 0
    while True:
        if wcswidth(text[:length]) >= screen_columns() * ratio:
            break
        length += 2
    return text[:length - 1] + "…'"


def history_hint(messages, parameters):
    if messages is None or len(messages) == 0:
        return
    ratio = 0.6
    for msg in messages:
        print(f"{msg['role'].capitalize():>9}: {output_with_ration(repr(msg['content']), ratio)}")
    print("======================================")
    print(json.dumps(parameters, indent=2))
    print("======================================")


def main():
    conversation = []
    # see more about parameters at https://console.groq.com/docs/reasoning
    parameters = {
        "model": "deepseek-r1-distill-llama-70b",
        # Controls randomness in responses. Lower values make responses more deterministic. Recommended range: 0.5-0.7 to prevent repetitions or incoherent outputs
        "temperature": 0.5,
        # Maximum length of model's response. Default may be too low for complex reasoning - consider increasing for detailed step-by-step solutions
        "max_completion_tokens": 6000,
        # Controls diversity of token selection
        "top_p": 0.95,
        # Enables response streaming
        "stream": True,
        # Includes reasoning within think tags in the content.
        "reasoning_format": "raw"
    }
    # Limit of model [deepseek-r1-distill-llama-70b]
    #  -  tokens per minute: 6K
    #  -  see more at https://console.groq.com/settings/limits

    # load conversation history if conversation_id is provided
    args = sys.argv
    if len(args) > 1:
        res = load_conversation(args[1])
        if res:
            conversation = res["messages"]
            parameters = res["parameters"]
            history_hint(conversation, parameters)

    conversation_id = uuid.uuid4().hex[:8]
    cur_min = datetime.now().strftime("%m_%d_%H_%M")
    log_filename = f"logs/{cur_min}-{conversation_id}.json"
    os.makedirs("logs", exist_ok=True)

    if len(conversation) > 0:
        log_interaction(log_filename, {
            "time": datetime.now().isoformat(),
            "messages": conversation,
            "parameters": parameters
        })

    print(f"Chat with deepseek-r1-distill-llama-70b (Groq). Type 'qq' to quit.")
    print(f"Current Conversation ID: {conversation_id}")
    while True:
        set_thinking(True)
        user_input = input(">>> ")
        if user_input.strip() == "":
            continue
        if user_input.strip().lower() == "qq":
            print(f"Bye. cid = {conversation_id}")
            break
        conversation.append({"role": "user", "content": user_input})
        log_interaction(log_filename, {
            "time": datetime.now().isoformat(),
            "messages": conversation,
            "parameters": parameters
        })

        # Send the conversation to the model
        try:
            completion = client.chat.completions.create(
                model=parameters["model"],
                messages=conversation,
                temperature=parameters["temperature"],
                max_completion_tokens=parameters["max_completion_tokens"],
                top_p=parameters["top_p"],
                stream=parameters["stream"],
                reasoning_format=parameters["reasoning_format"]
            )
        except Exception as e:
            print(f"API call failed: {str(e)}\n\nAbort. cid = {conversation_id}")
            break

        # Print the response
        response = ""
        for chunk in completion:
            tok = chunk.choices[0].delta.content or ""
            response += tok
            # 1. plain text
            # print(tok, end="")
            # 2. render markdown in the terminal
            render_single_line(tok)
            # 3. log the token
            append_file(repr(tok))
        print('\n\n')

        # Log the conversation
        conversation.append(
            {"role": "assistant", "content": response})
        log_interaction(log_filename, {
            "time": datetime.now().isoformat(),
            "messages": conversation,
            "parameters": parameters
        })


if __name__ == "__main__":
    main()
