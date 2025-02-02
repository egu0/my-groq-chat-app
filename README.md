# My Groq Chat App

## 使用

### 1. 创建一个 `.env` 文件，内容如下

[获取密钥](https://console.groq.com/keys)

```env
GROQ_API_KEY=
```

### 2. 安装依赖

```sh
pip install groq
```

### 3. 运行

```sh
python app.py
```

## 基本调用

```py
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq()
completion = client.chat.completions.create(
    model="deepseek-r1-distill-llama-70b",
    messages=[
        {
            "role": "user",
            "content": "How many r's are in the word strawberry?"
        }
    ],
    temperature=0.6,
    max_completion_tokens=1024,
    top_p=0.95,
    stream=True,
    reasoning_format="raw"
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")
