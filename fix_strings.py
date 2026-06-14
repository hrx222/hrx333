#!/usr/bin/env python3
import re

with open('/workspace/src/data/projects.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the problematic line 1848
old_line = "        explanation: 'plotly_dark' 是Plotly内置的暗色主题；'ggplot2' 是R语言风格主题；'dark' 不是有效模板名；可以组合多个主题。',"
new_line = '        explanation: "plotly_dark 是Plotly内置的暗色主题; ggplot2 是R语言风格主题; dark 不是有效模板名; 可以组合多个主题。",'

content = content.replace(old_line, new_line)

with open('/workspace/src/data/projects.ts', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done')
