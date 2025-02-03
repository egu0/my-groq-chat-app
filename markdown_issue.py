from pygments import highlight
from pygments.lexers import MarkdownLexer
from pygments.formatters import Terminal256Formatter
from pygments.styles import get_all_styles


markdown = """
# Title

This is a paragraph with **bold** and *italic* text.

## Subtitle

This is another paragraph with a [link](https://example.com).

- item 1
- item 2
- item 3

```python
print('Hello, World!')
```

> This is a blockquote.

This is the end of the document.
"""

styles = list(get_all_styles())
# ['abap', 'algol', 'algol_nu', 'arduino', 'autumn', 'bw', 'borland', 'colorful', 'default', 'dracula', 'emacs', 'friendly_grayscale', 'friendly', 'fruity', 'github-dark', 'gruvbox-dark', 'gruvbox-light', 'igor', 'inkpot', 'lightbulb', 'lilypond', 'lovelace', 'manni', 'material',
#     'monokai', 'murphy', 'native', 'nord-darker', 'nord', 'one-dark', 'paraiso-dark', 'paraiso-light', 'pastie', 'perldoc', 'rainbow_dash', 'rrt', 'sas', 'solarized-dark', 'solarized-light', 'staroffice', 'stata-dark', 'stata-light', 'tango', 'trac', 'vim', 'vs', 'xcode', 'zenburn']

highlighted_text = highlight(
    markdown, MarkdownLexer(), Terminal256Formatter(style='solarized-light'))
print(highlighted_text)
