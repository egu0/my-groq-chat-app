from io import BytesIO, StringIO

from pygments import highlight
from pygments.lexers import MarkdownLexer
from pygments.formatters import Terminal256Formatter
from pygments.styles import get_all_styles

markdown = """
<think>

这是一个Markdown文档示例，包含了常见的Markdown语法和格式。

</think>

# 随机生成的Markdown示例

## 1. 标题示例

### 1.1 一级标题
#### 1.1.1 二级标题
##### 1.1.1.1 三级标题

## 2. 列表示例

### 2.1 无序列表
- 项目1
- 项目2
- 子项目1
- 子项目2
- 项目3

### 2.2 有序列表
1. 第一项
2. 第二项
1. 子项1
2. 子项2
3. 第三项

## 3. 表格示例

| 列1 | 列2 | 列3 |
|------|------|------|
| 单元格1 | 单元格2 | 单元格3 |
| 单元格4 | 单元格5 | 单元格6 |
| 单元格7 | 单元格8 | 单元格9 |

## 4. 代码块示例

```python
def hello_world():
print("Hello, World!")

hello_world()
```

## 5. 数学公式示例

### 5.1 行内公式
Euler公式：$e^{i\pi} = -1$

### 5.2 独立公式
$$
f(x) = \int_{0}^{\infty} \frac{\sin(x)}{x} \, dx
$$

### 5.3 矩阵示例
$$
\begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix}
$$

## 6. 引用示例

> 这是一个引用段落，引用自某位伟人。
> “想象力比知识更重要，因为知识是有限的，而想象力概括着世界的一切。”
> —— 阿尔伯特·爱因斯坦

## 7. 链接示例

[百度](https://www.baidu.com)
[谷歌](https://www.google.com)

## 8. 图片示例

![Markdown Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Markdown-mark.svg
/208px-Markdown-mark.svg.png)

## 9. 强调示例

*斜体*
**加粗**
***斜体加粗***
~~删除线~~

## 10. 分割线示例

---
上面是一个分割线
"""

styles = list(get_all_styles())
# ['abap', 'algol', 'algol_nu', 'arduino', 'autumn', 'bw', 'borland', 'colorful', 'default', 'dracula', 'emacs', 'friendly_grayscale', 'friendly', 'fruity', 'github-dark', 'gruvbox-dark', 'gruvbox-light', 'igor', 'inkpot', 'lightbulb', 'lilypond', 'lovelace', 'manni', 'material',
#     'monokai', 'murphy', 'native', 'nord-darker', 'nord', 'one-dark', 'paraiso-dark', 'paraiso-light', 'pastie', 'perldoc', 'rainbow_dash', 'rrt', 'sas', 'solarized-dark', 'solarized-light', 'staroffice', 'stata-dark', 'stata-light', 'tango', 'trac', 'vim', 'vs', 'xcode', 'zenburn']

if __name__ == '__main__':
    #highlighted_text = highlight(
    #    markdown, MarkdownLexer(), Terminal256Formatter(style='solarized-light'))
    #print(highlighted_text)

    ########################

    # lexer
    lexer = MarkdownLexer()
    tks = lexer.get_tokens(markdown)  # generator, 不可二次迭代, 会被消耗
    # 转换为 list, 以便多次迭代
    tks = list(tks)
    for tk in tks:
        print(tk)

    print("--------------------")

    # formatter
    formatter = Terminal256Formatter(style='solarized-light')
    outfile = getattr(formatter, 'encoding', None) and BytesIO() or StringIO()
    formatter.format(tks, outfile)
    highlighted_content = outfile.getvalue()
    # print(repr(highlighted_content))
    print(highlighted_content)
