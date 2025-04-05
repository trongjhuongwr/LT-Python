import random

"""
1. Write a program to check a person is eligible for voting or not (sacceptage from user)
"""
def ex_01():
    age = int(input("Enter your age: "))
    if age >= 18:
        print(f"Your age is {age}")
        print("Your age is eligible for voting")
    else:
        print(f"Your age is {age}")
        print("Your age is not eligible for voting")


"""
2. Write a program to check whether a number entered by user is even or odd.
"""
def ex_02():
    number = int(input("Enter the number: "))
    if number % 2 == 0:
        print(f"The number {number} is even.")
    else:
        print(f"The number {number} is odd.")


"""
3. Write a program to check whether a number is divisible by 7 or not.
"""
def ex_03():
    number = int(input("Enter the number: "))
    if number % 7 == 0:
        print(f"The number {number} is divisible by 7.")
    else:
        print(f"The number {number} is not divisible by 7.")


"""
4. Write a program to check the last digit of a number (entered by user) is divisible by 3 or not.
"""
def ex_04():
    number = input("Enter the number: ")
    the_last_digit = number[-1:]
    if the_last_digit % 3 == 0:
        print(f"The last digit of {number} is divisible by 3.")
    else:
        print(f"The last digit of {number} is not divisible by 3.")


"""
5. Write a Python program to guess a number between 1 and 9.
"""
def ex_05():
    num = random.randint(1, 9)
    guess_num = int(input("Guess a number from 1 to 9: "))

    if num == guess_num:
        print("Damn, you are genius")
    else:
        print(f"Haha, that's wrong. You guess {guess_num}, but actualyy is {num}")


"""
6. Write a program to accept a number from 1 to 7 and display the name of the day like 1 for Sunday, 2 for Monday and so on.
"""
def ex_06():
    num = int(input("Enter any no. from 1 to 7 to display day of the week : "))

    if num == 1:
        print('Sunday')
    elif num == 2:
        print('Monday')
    elif num == 3:
        print('Tuesday')
    elif num == 4:
        print('Wednesday')
    elif num == 5:
        print('Thursday')
    elif num == 6:
        print('Friday')
    elif num == 7:
        print('Saturday')
    else:
        print('Invalid number !')



if __name__ == '__main__':
    ex_01()
    # ex_02()
    # ex_03()
    # ex_04()
    # ex_05()
    # ex_06()
