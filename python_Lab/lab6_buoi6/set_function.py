# Set
# 1. Write a Python program to find the maximum and minimum values in a set.
# 2. Write a Python program to check if a given value is present in a set or not.
# 3. Write a Python program to check if two given sets have no elements in common.
# 4. Write a Python program to find all the unique words and count the frequency of occurrence from a given list of strings. Use Python set data type.
# 5. Given two sets of numbers, write a Python program to find the missing numbers in the second set as compared to the first and vice versa. Use the Python set.

def ex1():
    sample_set = {5, 2, 8, 1, 9}
    return max(sample_set), min(sample_set)

def ex2():
    sample_set = {1, 3, 5, 7, 9}
    value = 5
    return value in sample_set

def ex3():
    set1 = {1, 2, 3}
    set2 = {4, 5, 6}
    return set1.isdisjoint(set2)

def ex4():
    words = ["apple", "banana", "apple", "orange", "banana", "apple"]
    unique_words = set(words)
    frequency = {word: words.count(word) for word in unique_words}
    return frequency

def ex5():
    set1 = {1, 2, 3, 4, 5}
    set2 = {3, 4, 5, 6, 7}
    missing_in_set2 = set1 - set2
    missing_in_set1 = set2 - set1
    return missing_in_set2, missing_in_set1
