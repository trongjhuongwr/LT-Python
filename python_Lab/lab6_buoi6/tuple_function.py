# Tuple
# 1. to create a tuple of numbers and print one item.
# 2. to unpack a tuple into several variables.
# 3. to add an item to a tuple.
# 4. to find the index of an item in a tuple.
# 5. to find the repeated items of a tuple

def ex1():
    tuple_numbers = tuple(('one', 'two', 'three'))
    print(tuple_numbers[1])

def ex2():
    tuple_numbers = tuple(('1', '2', '3'))
    (one, two, three) = tuple_numbers
    print(f'one: {one}')

def ex3():
    tuple_numbers = tuple(('one', 'two', 'three'))
    new_number = ('four', 'five', 'six')
    tuple_numbers += new_number
    print(tuple_numbers)

def ex4():
    tuple_numbers = ("one", "two", "three")
    print('one' in tuple_numbers)
    print('four' in tuple_numbers)

def ex5():
    tuple_numbers = ("one", "two", "three", "six", "five", "six")
    repeat_items = []
    for number in tuple_numbers:
        count = tuple_numbers.count(number)
        if count >= 2 and number not in repeat_items:
            repeat_items.append(number)

    print(repeat_items)