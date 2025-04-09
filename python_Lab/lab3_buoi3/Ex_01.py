import random

"""
1. Write a program that prompts the user to enter base and height of the triangle and 
calculate an area of this triangle (area = 0.5 x b x h).
"""
def ex01():
    base = float(input("Enter the base of a triangle: "))
    height = float(input("Enter the height of a triangle: "))

    #calculate the area of triangle
    area = 0.5 * base * height
    print(f"Area of the triangle with base = {base} and height = {height} is {area}")


"""
2. Write a script that prompts the user to enter side a, side b, and side c of the triangle. 
Calculate the perimeter of the triangle (perimeter = a + b + c).
"""
def ex02():
    a = float(input("Enter side a: "))
    b = float(input("Enter side b: "))
    c = float(input("Enter side c: "))

    #Calculate the perimeter of triangle
    perimeter = a + b + c
    print(f"Perimeter of triangle with side a = {a}, side b = {b}, side c = {c} is {perimeter}")


"""
3. Get length and width of a rectangle using prompt. 
Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
"""
def ex03():
    l = float(input("Enter the length of a retangle: "))
    w = float(input("Enter the width of a retangle: "))

    #Calculate area
    area = l * w

    #Calculate perimeter
    perimeter = 2 * (l + w)

    print(f"area with length = {l} and width = {w} = {area}")
    print(f"perimeter with length = {l} and width = {perimeter}")


"""
4. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
"""
def ex04():
    r = float(input("Enter the radius of a circle: "))
    pi = 3.14

    # Calculate the area
    area = pi * r**2
    # Calculate the circumference
    c = 2 * pi * r

    print(f"The area with radius = {r} is {area}")
    print(f"The circumference with radius = {r} is {c}")


"""
5. Calculate the slope, x-intercept and y-intercept of y = 2x -2
"""
def ex05():
    # For equation y = mx + b
    m = 2  # slope
    b = -2  # y-intercept

    # Calculate x-intercept
    x_intercept = -b / m

    # Print results
    print(f"Equation: y = {m}x + {b}")
    print(f"Slope (m): {m}")
    print(f"Y-intercept: (0, {b})")
    print(f"X-intercept: ({x_intercept}, 0)")


"""
6. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
"""
def ex_06():
    return 0



"""
7. Compare the slopes in tasks 8 and 9.
"""
def ex_07():
    return 0


"""
8. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
"""
def ex_08():
    return 0

"""
9. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
"""
def ex_09():
    return 0

"""
10. Use and operator to check if 'on' is found in both 'python' and 'dragon'
"""
def ex_10():
    return 0

"""
11. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
"""
def ex_11():
    return 0


def ex_12():
    return 0


"""
13. Find the length of the text python and convert the value to float and convert it to string
"""
def ex_13():
    return 0

"""
14. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
"""
def ex_14():
    return 0


"""
15. Writs a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
"""
def ex_15():
    return 0


"""
16. Write a script that prompts the user to enter number of years. 
Calculate the number of seconds a person can live. Assume a person can live hundred years
"""
def ex_16():
    return 0




if __name__ == '__main__':
    #Operators Exercises
    ex01()
    # ex02()
    # ex03()
    # ex04()
    # ex05()
    # ex_06()
    # ex_07()
    # ex_08()
    # ex_09()
    # ex_10()
    # ex_11()
    # ex_12()
    # ex_13()
    # ex_14()
    # ex_15()
    # ex_16()
