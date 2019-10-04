#!/usr/bin/python3
""" Module: 5-text_indentation
Contain function text_indentation that prints a text with 2 new lines after
each of given characters
    Testing: use tests/5-text_indentation.txt with doctest()
"""


def text_indentation(text):
    """prints a text with 2 new lines after each of given characters
    Arg:
        text (str): string text
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    count = 0
    count_b = 0
    for esp in reversed(range(len(text))):
        if text[esp] == " ":
            count += 1
        else:
            break
    for esp_beg in range(len(text)):
        if text[esp_beg] == " ":
            count_b += 1
        else:
            break
    if count != 0:
        cpy_text = text[count_b:-count]
    else:
        cpy_text = text[count_b:]
    try:
        while cpy_text[i]:
            if cpy_text[i] == '.' or cpy_text[i] == '?' or cpy_text[i] == ':':
                print(cpy_text[i])
                i += 1
                for e in range(len(cpy_text[i:])):
                    if cpy_text[i] == " ":
                        i += 1
                    else:
                        break
                print()
                continue
            print(cpy_text[i], end="")
            i += 1
    except:
        pass
