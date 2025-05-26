import random
from itertools import permutations


# 1. Write a  Python program to sum all the items in a list.
def ex1(lst):
    sum_list = sum(lst)
    print(sum_list)


# 2. Write a  Python program to multiply all the items in a list.
def ex2(lst):
    result = 1
    for item in lst:
        result *= item
    print(result)


# 3. Write a Python program to get the largest number from a list.
def ex3(lst):
    print(max(lst))


# 4. Write a Python program to get the smallest number from a list.
def ex4(lst):
    print(min(lst))


# 5. Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2
def ex5(lst):
    count = 0
    for s in lst:
        if len(s) >= 2 and s[0] == s[-1]:
            count += 1
    print(count)


# 6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
def ex6(lst):
    lst.sort(key=lambda x: x[-1])
    print(lst)


# 7. Write a  Python program to remove duplicates from a list.
def ex7(lst):
    unique_list = list(set(lst))
    print(unique_list)


# 8. Write a  Python program to check if a list is empty or not.
def ex8(lst):
    print(not bool(lst))


# 9. Write a Python program to clone or copy a list.
def ex9(lst):
    new_list = lst.copy()
    print(new_list)


# 10. Write a Python program to find the list of words that are longer than n from a given list of words.
def ex10(words, n):
    result = [word for word in words if len(word) > n]
    print(result)


# 11. Write a Python function that takes two lists and returns True if they have at least one common member.
def ex11(list1, list2):
    print(bool(set(list1) & set(list2)))


# 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']
def ex12(lst):
    indices = [0, 4, 5]
    new_lst = [v for i, v in enumerate(lst) if i not in indices]
    print(new_lst)


# 13. Write a  Python program to generate a 3*4*6 3D array whose each element is *.
def ex13():
    array = [[['*' for _ in range(6)] for _ in range(4)] for _ in range(3)]
    print(array)


# 14. Write a  Python program to print the numbers of a specified list after removing even numbers from it.
def ex14(lst):
    odd_list = [num for num in lst if num % 2 != 0]
    print(odd_list)


# 15. Write a Python program to shuffle and print a specified list.
def ex15(lst):
    random.shuffle(lst)
    print(lst)


# 16. Write a Python program to generate and print a list of the first and last 5 elements where the values are square numbers between 1 and 30 (both included).
def ex16():
    squares = [i**2 for i in range(1, 31)]
    result = squares[:5] + squares[-5:]
    print(result)


# 17. Write a Python program to check if each number is prime in a given list of numbers. Return True if all numbers are prime otherwise False.
# Sample Data:
# ([0, 3, 4, 7, 9]) -> False
# ([3, 5, 7, 13]) -> True
# ([1, 5, 3]) -> False
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def ex17(lst):
    print(all(is_prime(num) for num in lst))


# 18. Write a  Python program to generate all permutations of a list in  Python.
def ex18(lst):
    print(list(permutations(lst)))


# 19. Write a Python program to calculate the difference between the two lists.
def ex19(list1, list2):
    diff = list(set(list1) - set(list2))
    print(diff)


# 20. Write a Python program to access the index of a list.
def ex20(lst):
    for index, value in enumerate(lst):
        print(f"Index: {index}, Value: {value}")


# 21. Write a Python program to convert a list of characters into a string.
def ex21(char_list):
    print(''.join(char_list))


# 22. Write a Python program to find the index of an item in a specified list.
def ex22(lst, item):
    print(lst.index(item))


# 23. Write a Python program to flatten a shallow list.
def ex23(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, list):
            flat_list.extend(item)
        else:
            flat_list.append(item)
    print(flat_list)


# 24. Write a Python program to append a list to the second list.
def ex24(list1, list2):
    list1.extend(list2)
    print(list1)


# 25. Write a Python program to select an item randomly from a list.
def ex25(lst):
    print(random.choice(lst))


# 26. Write a  Python program to check whether two lists are circularly identical.
def ex26(list1, list2):
    print(' '.join(map(str, list2)) in ' '.join(map(str, list1 * 2)))


# 27. Write a  Python program to find the second smallest number in a list.
def ex27(lst):
    unique_sorted = sorted(set(lst))
    print(unique_sorted[1])


# 28. Write a Python program to find the second largest number in a list.
def ex28(lst):
    unique_sorted = sorted(set(lst), reverse=True)
    print(unique_sorted[1])


# 29. Write a Python program to get unique values from a list.
def ex29(lst):
    print(list(set(lst)))


# 30. Write a Python program to get the frequency of elements in a list.
def ex30(lst):
    frequency = {}
    for item in lst:
        frequency[item] = frequency.get(item, 0) + 1
    print(frequency)


# 31. Write a Python program to count the number of elements in a list within a specified range.
def ex31(lst, start, end):
    count = sum(start <= num <= end for num in lst)
    print(count)


# 32. Write a Python program to check whether a list contains a sublist.
def ex32(main_list, sub_list):
    n = len(sub_list)
    for i in range(len(main_list)-n+1):
        if main_list[i:i+n] == sub_list:
            print(True)
            return
    print(False)


# 33. Write a  Python program to generate all sublists of a list.
def ex33(lst):
    sublists = []
    for start in range(len(lst)):
        for end in range(start+1, len(lst)+1):
            sublists.append(lst[start:end])
    print(sublists)


# 34. Write a  Python program that uses the Sieve of Eratosthenes method to compute prime numbers up to a specified number.
# Note: In  mathematics, the sieve of Eratosthenes, (Ancient Greek: κόσκινον, Ἐρατοσθένους, kóskinon Eratosthénous) one of a number of prime number sieves, is a simple, ancient algorithm for finding all prime numbers up to any given limit.
def ex34(n):
    sieve = [True] * (n+1)
    sieve[0:2] = [False, False]
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            sieve[i*i:n+1:i] = [False]*len(sieve[i*i:n+1:i])
    primes = [i for i, is_prime in enumerate(sieve) if is_prime]
    print(primes)


# 35. Write a Python program to create a list by concatenating a given list with a range from 1 to n.
# Sample list : ['p', 'q']
# n =5
# Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
def ex35(lst, n):
    result = [f"{item}{i}" for i in range(1, n+1) for item in lst]
    print(result)


# 36. Write a  Python program to get a variable with an identification number or string.
def ex36(var):
    print(id(var))


# 37. Write a  Python program to find common items in two lists.
def ex37(list1, list2):
    print(bool(set(list1) & set(list2)))


# 38. Write a Python program to change the position of every n-th value to the (n+1)th in a list.
# Sample list: [0,1,2,3,4,5]
# Expected Output: [1, 0, 3, 2, 5, 4]
def ex38(lst):
    for i in range(0, len(lst)-1, 2):
        lst[i], lst[i+1] = lst[i+1], lst[i]
    print(lst)


# 39. Write a Python program to convert a list of multiple integers into a single integer.
# Sample list: [11, 33, 50]
# Expected Output: 113350
def ex39(lst):
    result = int(''.join(map(str, lst)))
    print(result)


# 40. Write a Python program to split a list based on the first character of a word.
def ex40(lst):
    groups = {}
    for word in lst:
        key = word[0]
        groups.setdefault(key, []).append(word)
    print(groups)


# 41. Write a  Python program to create multiple lists.
def ex41():
    list1 = []
    list2 = [1,2,3]
    list3 = ['a','b']
    return [list1, list2, list3]


# 42. Write a Python program to find missing and additional values in two lists.
# Sample data : Missing values in second list: b,a,c
# Additional values in second list: g,h
def ex42(list1, list2):
    missing = set(list1) - set(list2)
    additional = set(list2) - set(list1)
    print(f"Missing: {missing}, Additional: {additional}")


# 43. Write a  Python program to split a list into different variables.
def ex43(lst):
    var1, var2, var3 = lst[0], lst[1], lst[2]
    print(var1, var2, var3)


# 44. Write a Python program to generate groups of five consecutive numbers in a list.
def ex44():
    groups = [list(range(i, i+5)) for i in range(1, 20, 5)]
    print(groups)

# 45. Write a Python program to convert a pair of values into a sorted unique array.
def ex45(lst):
    unique_array = sorted(set(num for pair in lst for num in pair))
    print(unique_array)


# 46. Write a Python program to select the odd items from a list.
def ex46(lst):
    print(lst[1::2])


# 47. Write a Python program to insert an element before each element of a list.
def ex47(lst, element):
    new_list = [element for _ in range(len(lst)*2)]
    new_list[1::2] = lst
    print(new_list)


# 48. Write a  Python program to print nested lists (each list on a new line) using the print() function.
def ex48(nested_list):
    for sublist in nested_list:
        print(sublist)


# 49. Write a Python program to convert a list to a list of dictionaries.
# Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
# Expected Output: [{'color_name': 'Black', 'color_code': '#000000'}, {'color_name': 'Red', 'color_code': '#FF0000'}, {'color_name': 'Maroon', 'color_code': '#800000'}, {'color_name': 'Yellow', 'color_code': '#FFFF00'}]
def ex49(keys, values):
    print([dict(zip(keys, values))])


# 50. Write a  Python program to sort a list of nested dictionaries.
def ex50(lst, key):
    print(sorted(lst, key=lambda x: x[key]))


if __name__ == '__main__':
    integer_list = []
    for i in range(10):
        a = random.randint(1, 100)
        integer_list.append(a)
    print(f"Integer List: {integer_list}")
    numbers = [3, 1, 4, 1, 5, 9, 2, 6]
    strings = ['abc', 'xyz', 'aba', '1221', 'a']
    tuples = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    nested_list = [[1, 2], [3, 4, 5], [6]]
    color_names = ["Black", "Red", "Maroon", "Yellow"]
    color_codes = ["#000000", "#FF0000", "#800000", "#FFFF00"]

    print("=== Bài 1:  ===")
    ex1(integer_list)

    print("=== Bài 2:  ===")
    ex2(integer_list)

    print("=== Bài 3: Largest number ===")
    ex3(numbers)  # Expected: 9

    print("\n=== Bài 4: Smallest number ===")
    ex4(numbers)  # Expected: 1

    print("\n=== Bài 5: Count special strings ===")
    ex5(strings)  # Expected: 2

    print("\n=== Bài 6: Sort tuples by last element ===")
    ex6(tuples)  # Expected: [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

    print("\n=== Bài 7: Remove duplicates ===")
    ex7([1, 2, 2, 3, 3, 3])  # Expected: [1, 2, 3]

    print("\n=== Bài 8: Check empty list ===")
    ex8([])  # Expected: True
    ex8([1])  # Expected: False

    print("\n=== Bài 9: Clone list ===")
    ex9(numbers)  # Expected: Bản sao của numbers

    print("\n=== Bài 10: Words longer than n ===")
    ex10(["apple", "cat", "computer", "dog"], 3)  # Expected: ['apple', 'computer']

    print("\n=== Bài 11: Common elements ===")
    ex11([1, 2, 3], [3, 4, 5])  # Expected: True
    ex11([1, 2], [3, 4])  # Expected: False

    print("\n=== Bài 12: Remove elements ===")
    ex12(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'])  # Expected: ['Green', 'White', 'Black']

    print("\n=== Bài 13: 3D array ===")
    ex13()  # Expected: Mảng 3x4x6 chứa toàn dấu *

    print("\n=== Bài 14: Remove even numbers ===")
    ex14([1, 2, 3, 4, 5, 6])  # Expected: [1, 3, 5]

    print("\n=== Bài 15: Shuffle list ===")
    ex15([1, 2, 3, 4, 5])  # Output ngẫu nhiên

    print("\n=== Bài 16: First and last 5 squares ===")
    ex16()  # Expected: [1, 4, 9, 16, 25, 676, 729, 784, 841, 900]

    print("\n=== Bài 17: Check all primes ===")
    ex17([3, 5, 7, 13])  # True
    ex17([0, 3, 4, 7])  # False

    print("\n=== Bài 18: Permutations ===")
    ex18([1, 2, 3])  # Tất cả hoán vị của 3 phần tử

    print("\n=== Bài 19: List difference ===")
    ex19([1, 2, 3, 4], [3, 4, 5])  # Expected: [1, 2]

    print("\n=== Bài 20: Access index ===")
    ex20(['a', 'b', 'c'])  # In index và giá trị

    print("\n=== Bài 21: List to string ===")
    ex21(['H', 'e', 'l', 'l', 'o'])  # Expected: 'Hello'

    print("\n=== Bài 22: Find index ===")
    ex22(['apple', 'banana', 'cherry'], 'banana')  # Expected: 1

    print("\n=== Bài 23: Flatten list ===")
    ex23([[1, 2], [3, [4, 5]]])  # Expected: [1, 2, 3, [4, 5]]

    print("\n=== Bài 24: Extend list ===")
    ex24([1, 2], [3, 4])  # Expected: [1, 2, 3, 4]

    print("\n=== Bài 25: Random choice ===")
    ex25(['rock', 'paper', 'scissors'])  # Chọn ngẫu nhiên

    print("\n=== Bài 26: Circular check ===")
    ex26([1, 2, 3], [2, 3, 1])  # True
    ex26([1, 2, 3], [3, 2, 1])  # False

    print("\n=== Bài 27: Second smallest ===")
    ex27([5, 2, 3, 1, 1, 4])  # Expected: 2

    print("\n=== Bài 28: Second largest ===")
    ex28([5, 2, 3, 1, 4])  # Expected: 4

    print("\n=== Bài 34: Sieve of Eratosthenes ===")
    ex34(30)  # Các số nguyên tố <=30

    print("\n=== Bài 38: Swap every pair ===")
    ex38([0, 1, 2, 3, 4, 5])  # Expected: [1, 0, 3, 2, 5, 4]

    print("\n=== Bài 49: List of dicts ===")
    ex49(['color_name', 'color_code'], [color_names, color_codes])