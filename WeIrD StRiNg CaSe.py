# Write a function toWeirdCase (weirdcase in Ruby) that accepts a string, and returns the same string with all even indexed characters in each word upper cased, 
# and all odd indexed characters in each word lower cased. The indexing just explained is zero based, so the zero-ith index is even, therefore that character should be upper cased.

# The passed in string will only consist of alphabetical characters and spaces(' '). 
# Spaces will only be present if there are multiple words. Words will be separated by a single space(' ').

# https://www.codewars.com/kata/52b757663a95b11b3d00062d/train/python

def to_weird_case(string):
    string_new = list(string)
    index = 0
    for i in range(len(string_new)):
        if ord(string_new[i]) == 32:
            index = 0 
            pass
        elif index%2 == 0:
            string_new[i] = string_new[i].upper()
            index += 1
        elif index%2 == 1:
            string_new[i] = string_new[i].lower()
            index += 1
    string_new = ''.join(string_new)
    return string_new

print(to_weird_case('This'))
print(to_weird_case('is'))
print(to_weird_case('This is a test'))


def to_weird_case_word(string):
    return "".join(c.upper() if i%2 == 0 else c for i, c in enumerate(string.lower()))

def to_weird_case_best(string):
    return " ".join(to_weird_case_word(str) for str in string.split())

print(to_weird_case_best('This'))
print(to_weird_case_best('is'))
print(to_weird_case_best('This is a test'))