import random

# 1. Write a  Python program to sum all the items in a list.
def ex1(list):
    sum_list = sum(list)
    print(sum_list)

# 2. Write a  Python program to multiply all the items in a list.
def ex2(list):
    result = 1
    for item in list:
        result *= item
    print(result)

# 3. Write a Python program to get the largest number from a list.
def ex3(list):
    pass

# 4. Write a Python program to get the smallest number from a list.

# 5. Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

# 6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

# 7. Write a  Python program to remove duplicates from a list.

# 8. Write a  Python program to check if a list is empty or not.

# 9. Write a Python program to clone or copy a list.

# 10. Write a Python program to find the list of words that are longer than n from a given list of words.

# 11. Write a Python function that takes two lists and returns True if they have at least one common member.

# 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']

# 13. Write a  Python program to generate a 3*4*6 3D array whose each element is *.

# 14. Write a  Python program to print the numbers of a specified list after removing even numbers from it.

# 15. Write a Python program to shuffle and print a specified list.

# 16. Write a Python program to generate and print a list of the first and last 5 elements where the values are square numbers between 1 and 30 (both included).

# 17. Write a Python program to check if each number is prime in a given list of numbers. Return True if all numbers are prime otherwise False.
# Sample Data:
# ([0, 3, 4, 7, 9]) -> False
# ([3, 5, 7, 13]) -> True
# ([1, 5, 3]) -> False

# 18. Write a  Python program to generate all permutations of a list in  Python.

# 19. Write a Python program to calculate the difference between the two lists.

# 20. Write a Python program to access the index of a list.

# 21. Write a Python program to convert a list of characters into a string.

# 22. Write a Python program to find the index of an item in a specified list.

# 23. Write a Python program to flatten a shallow list.

# 24. Write a Python program to append a list to the second list.

# 25. Write a Python program to select an item randomly from a list.

# 26. Write a  Python program to check whether two lists are circularly identical.

# 27. Write a  Python program to find the second smallest number in a list.

# 28. Write a Python program to find the second largest number in a list.

# 29. Write a Python program to get unique values from a list.

# 30. Write a Python program to get the frequency of elements in a list.

# 31. Write a Python program to count the number of elements in a list within a specified range.

# 32. Write a Python program to check whether a list contains a sublist.

# 33. Write a  Python program to generate all sublists of a list.

# 34. Write a  Python program that uses the Sieve of Eratosthenes method to compute prime numbers up to a specified number.
# Note: In  mathematics, the sieve of Eratosthenes, (Ancient Greek: κόσκινον
# Ἐρατοσθένους, kóskinon Eratosthénous) one of a number of prime number sieves, is a simple, ancient algorithm for finding all prime numbers up to any given limit.

# 35. Write a Python program to create a list by concatenating a given list with a range from 1 to n.
# Sample list : ['p', 'q']
# n =5
# Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']

# 36. Write a  Python program to get a variable with an identification number or string.

# 37. Write a  Python program to find common items in two lists.

# 38. Write a Python program to change the position of every n-th value to the (n+1)th in a list.
# Sample list: [0,1,2,3,4,5]
# Expected Output: [1, 0, 3, 2, 5, 4]

# 39. Write a Python program to convert a list of multiple integers into a single integer.
# Sample list: [11, 33, 50]
# Expected Output: 113350

# 40. Write a Python program to split a list based on the first character of a word.

# 41. Write a  Python program to create multiple lists.

# 42. Write a Python program to find missing and additional values in two lists.
# Sample data : Missing values in second list: b,a,c
# Additional values in second list: g,h

# 43. Write a  Python program to split a list into different variables.

# 44. Write a Python program to generate groups of five consecutive numbers in a list.

# 45. Write a Python program to convert a pair of values into a sorted unique array.

# 46. Write a Python program to select the odd items from a list.

# 47. Write a Python program to insert an element before each element of a list.

# 48. Write a  Python program to print nested lists (each list on a new line) using the print() function.

# 49. Write a Python program to convert a list to a list of dictionaries.
# Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
# Expected Output: [{'color_name': 'Black', 'color_code': '#000000'}, {'color_name': 'Red', 'color_code': '#FF0000'}, {'color_name': 'Maroon', 'color_code': '#800000'}, {'color_name': 'Yellow', 'color_code': '#FFFF00'}]

# 50. Write a  Python program to sort a list of nested dictionaries.

if __name__ == '__main__':
    #string_list = ['abc', 'xyz', 'aba', '1221']
    integer_list = []
    for i in range(10):
        a = random.randint(1, 100)
        integer_list.append(a)
    print(f"Integer List: {integer_list}")


    ex1(integer_list)
    ex2(integer_list)
    #pass