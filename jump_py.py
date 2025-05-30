# -*- coding: utf-8 -*-
"""jump.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KTYCUcQJFhusyC4M5NYHFSUn6MYnpcqz
"""

# 1.Create a function that searches a string for the character 'x', uses break when found, and returns the position or -1 if not found.

def find_x_position(text):
    position = -1  # Default if 'x' is not found
    for i in range(len(text)):
        if text[i] == 'x':
            position = i
            break
    return position
print(find_x_position("hello"))

# 2.Write a function that processes a list of values but immediately returns False if any value is zero.


def process_values(values):
    for value in values:
        if value == 0:
            return False
    return True
print(process_values([1, 2, 3, 4]))

# 3.Create a function that counts non-space characters in a string but uses continue to skip vowels.
def count_non_space_non_vowels(text):
    count = 0
    vowels = 'aeiouAEIOU'
    for char in text:
        if char == ' ' or char in vowels:
            continue
        count += 1
    return count
print(count_non_space_non_vowels("aeiou"))