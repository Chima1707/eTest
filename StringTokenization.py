"""
Question 4
String Tokenization in Python
Write a function, tokenize_string(input_string, delimiter_list) that returns a list of strings that are separated by the
delimiters.
For example: tokenize_string("How now, Mrs. Brown Cow") returns ['How', 'now', 'Mrs', 'Brown', 'Cow']

"""
import re

def splitString(string1):
    pattern = re.compile(r'\W+')
    return pattern.split(string1)

print splitString('How now, Mrs. Brown Cow')