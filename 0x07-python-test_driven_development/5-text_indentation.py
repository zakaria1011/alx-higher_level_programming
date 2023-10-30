#!/usr/bin/python3
"""
print text with certain special caractere normes

"""
def text_indentation(text):
    """
    Print the input text with two newlines after each '.', '?', and ':' character.
    
    Args:
        text (str): The input text to be processed.
    
    Raises:
        TypeError: If the input is not a string.

    Prints the text with proper indentation, ensuring there are no spaces at the beginning or end of each printed line.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
