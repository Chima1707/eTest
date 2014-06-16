"""
Question 2.
Characters in Strings in Python
Implement a function with signature find_chars(string1, string2) that takes two strings and returns a string that
contains only the characters found in string1 and string two in the order that they are found in string1. Implement
a version of order N*N and one of order N

"""
def orderNByN(string1, string2):
    return ''.join([d for d in string1 if d in string2])


def orderNTimes(string1, string2):
    unique = set(string2)
    return ''.join([d for d in string1 if d in unique])


print orderNByN('peter','peterson')
print orderNTimes('peter', 'peterson')