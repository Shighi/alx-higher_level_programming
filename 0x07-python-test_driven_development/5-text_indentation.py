#!/usr/bin/python3
"""
Module for text_indentation function.
"""

def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation = ['.', '?', ':']
    result = ""
    for char in text:
        result += char
        if char in punctuation:
            result += "\n\n"
    
    # Remove spaces at the beginning of each line
    lines = result.split("\n")
    formatted_lines = [line.strip() for line in lines]
    print("\n".join(formatted_lines), end="")
