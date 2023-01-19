from sys import stdin
import re

input = stdin.readline

MAIN_START = '<main>'
MAIN_END = '</main>'
TITLE_START = '<div '
TITLE_END = '</div>'
P_START = '<p>'
P_END = '</p>'

tag_regex = re.compile('<(?:"[^"]*"[\'"]*|\'[^\']*\'[\'"]*|[^\'">])+>')
whitespace_regex = re.compile('\s\s+')
s = input().strip()
tags = tag_regex.findall(s)
tag_indexes = [x.start(0) for x in tag_regex.finditer(s)]


tag_stack = []
result = []

start_index = 0

for (tag, tag_index) in zip(tags, tag_indexes):
    if tag.startswith(MAIN_START):
        tag_stack.append(tag)
    elif tag.startswith(MAIN_END):
        tag_stack.pop()
    elif tag.startswith(TITLE_START):
        tag_stack.append(tag)
        result.append('title : '+tag.split('"')[1])
    elif tag.startswith(TITLE_END):
        tag_stack.pop()
    elif tag.startswith(P_START):
        tag_stack.append(tag)
        start_index = tag_index
    elif tag.startswith(P_END):
        tag_stack.pop()
        tmp = tag_regex.sub('', s[start_index+3:tag_index].strip())
        tmp = whitespace_regex.sub(' ', tmp)
        result.append(tmp)

[print(x) for x in result]
