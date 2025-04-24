import random

def ex1(list):
    sum_list = sum(list)
    print(sum_list)

def ex2(list):
    result = 1
    for item in list:
        result *= item
    print(result)

def ex3(list):
    pass


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