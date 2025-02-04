import os
import json
from datetime import datetime
from groq import Groq
from dotenv import load_dotenv
from markdown import append_file, render_single_line, set_thinking

load_dotenv()

client = Groq()


def log_interaction(log_filename, append):
    try:
        with open(log_filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []  # Initialize as an empty list if the file doesn't exist or is empty

    data.insert(0, append)

    with open(log_filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def main():
    conversation = []

    config = {
        "start_time": datetime.now().strftime("%Y-%m-%d-%H-%M-%S"),
        "parameters": {
            "model": "deepseek-r1-distill-llama-70b",
            # Controls randomness in responses. Lower values make responses more deterministic. Recommended range: 0.5-0.7 to prevent repetitions or incoherent outputs
            "temperature": 0.5,
            # Maximum length of model's response. Default may be too low for complex reasoning - consider increasing for detailed step-by-step solutions
            "max_completion_tokens": 4096,
            # Controls diversity of token selection
            "top_p": 0.95,
            # Enables response streaming
            "stream": True,
            # Includes reasoning within think tags in the content.
            "reasoning_format": "raw"
        }
        # 参考：https://console.groq.com/docs/reasoning
    }
    log_filename = f"logs/{config['start_time']}.json"
    os.makedirs("logs", exist_ok=True)

    print("Chat with deepseek-r1-distill-llama-70b (Groq). Type 'exit' to quit.")
    while True:
        set_thinking(True)
        user_input = input(">>> ")
        if user_input.strip() == "":
            continue
        if user_input.lower() == "exit":
            print("Bye.")
            break
        conversation.append({"role": "user", "content": user_input})
        log_interaction(log_filename, {
            "time": datetime.now().isoformat(),
            "messages": conversation,
            "parameters": config["parameters"]
        })

        # Send the conversation to the model
        try:
            completion = client.chat.completions.create(
                model=config["parameters"]["model"],
                messages=conversation,
                temperature=config["parameters"]["temperature"],
                max_completion_tokens=config["parameters"]["max_completion_tokens"],
                top_p=config["parameters"]["top_p"],
                stream=config["parameters"]["stream"],
                reasoning_format=config["parameters"]["reasoning_format"]
            )
        except Exception as e:
            print(f"API call failed: {str(e)}\n\nAbort.")
            break
        # Print the response
        response = ""
        for chunk in completion:
            tok = chunk.choices[0].delta.content or ""
            response += tok
            # 1. plain text
            # print(tok, end="")
            # 2. 逐行渲染返回的 markdown
            render_single_line(tok)
            # 3. 记录 repr 结果
            # print(repr(tok) + ',')
            append_file(repr(tok))
        print('\n\n')
        conversation.append({"role": "assistant", "content": response})
        # Log the conversation
        log_interaction(log_filename, {
            "time": datetime.now().isoformat(),
            "messages": conversation,
            "parameters": config["parameters"]
        })


if __name__ == "__main__":
    main()
