# 在终端中使用 DeepSeek (Groq)

[English](README_EN.md)

## 示例

![1](static/comparsion.png)

![2](static/dry-clothes.png)

![3](static/generate.png)

## 使用方法

Windows, Linux, MacOS 通用

### 1. 创建包含以下内容的 `.env` 文件

```env
GROQ_API_KEY=
```

[获取访问 Groq API 服务密钥](https://console.groq.com/keys)

### 2. 安装依赖

环境：俺用的 miniconda, python 3.11

```sh
pip install groq python-dotenv wcwidth pygments
```

### 3. 运行

```sh
python app.py
```

### 4. 配置快捷命令（此步非必须）

根据你使用的 shell 类型，配置一个 `aha` 命令，指向 `app.py` 文件。例如：

为 `~/.zshrc` 文件中添加：

```sh
aha() {
    (cd /path/to/your-repo/ && /path/of/your/python app.py "$@")
}
```

### 5. 使用

```sh
# 新回话
aha

# 继续上次的回话
aha <conversation_id>
```

## 基本示例

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
            "content": "How many Rs are in the word strawberry?"
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
```

[来源](https://console.groq.com/docs/reasoning)
