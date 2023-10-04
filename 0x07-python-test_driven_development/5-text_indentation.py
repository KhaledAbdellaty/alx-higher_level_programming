#!/usr/bin/python3
"""Defination of text_indentation function"""


def text_indentation(text):
    """a function that prints a text with 2
       new lines after each of
       these characters: ., ? and :

    Args:
        text (str): the text must be string.

    Raises:
        raise TypeError text must be a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    marks = [".", "?", ":"]
    lines = []
    current_line = ""
    cpy_text = text.replace("    ", "")

    for char in cpy_text:
        current_line += char
        if char in marks:
            lines.append(current_line.strip())
            lines.append("")
            current_line = ""

    if current_line:
        lines.append(current_line.strip())

    for i in range(len(lines)):
        if i == (len(lines) - 1):
            print(lines[i], end="")
        else:
            print(lines[i])
