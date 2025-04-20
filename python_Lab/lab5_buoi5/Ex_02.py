import os
import random
import math

def menu():
    print("--------------------------------MENU--------------------------------")
    print(" 1. In ra danh sách vừa tạo.")
    print(" 2. In đảo ngược danh sách.")
    print(" 3. Sắp xếp danh sách và in ra danh sách vừa sắp xếp (dùng sorted).")
    print(" 4. Tìm phần tử lớn nhất của danh sách và vị trí phần tử lớn nhất cuối cùng.")
    print(" 5. Đếm số lượng các phần tử bằng giá trị X nhập từ bàn phím. In ra các vị trí xuất hiện.")
    print(" 6. In ra vị trí các phần tử là số nguyên tố.")
    print(" 7. Tìm các số duy nhất (không trùng lặp) trong danh sách.")
    print(" 8. Liệt kê các giá trị xuất hiện trong mảng kèm theo số lần xuất hiện của nó.")
    print(" 9. In ra các đoạn con trong danh sách giảm liên tiếp.")
    print("10. Thoát")

    selection = int(input("Nhập lựa chọn của bạn: "))
    return selection

def generate_list(n):
    lst = []
    for i in range(n):
        a = random.randint(1, 100)
        lst.append(a)
    return lst

def choice(selection, list):
    if selection == 1:
        ex1(list)
    elif selection == 2:
        ex2(list)
    elif selection == 3:
        ex3(list)
    elif selection == 4:
        ex4(list)
    elif selection == 5:
        ex5(list)
    elif selection == 6:
        ex6(list)
    elif selection == 7:
        ex7(list)
    elif selection == 8:
        ex8(list)
    elif selection == 9:
        ex9(list)
    else:
        pass

def ex1(list):
    print(f"Danh sách: {list}")

def ex2(list):
    print(f"Danh sách: {list}")
    reverse_list = list[::-1]
    print(f"Danh sách đảo ngược: {reverse_list}")

def ex3(list):
    print(f"Danh sách: {list}")
    sort_list = sorted(list)
    print(f"Danh sách đã sắp xếp: {sort_list}")


def ex4(list):
    print(f"Danh sách: {list}")
    max = 0
    max_index = 0
    for i in range(len(list)):
        if list[i] >= max:
            max = list[i]
            max_index = i
    print(f"Phần tử lớn nhất là {max} và vị trí cuối cùng là {max_index}")


def ex5(list):
    print(f"Danh sách: {list}")
    count = 0
    X = int(input("Nhập giá trị phần tử muốn đếm: "))
    X_index = []
    for i in range(len(list)):
        if list[i] == X:
            count += 1
            X_index.append(i)
    print(f"Số lượng phần tử {X} là: {count} với các vị trí lần lượt là: {X_index}")

def ex6(list):
    print(f"Danh sách: {list}")
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, math.floor(math.sqrt(n))):
            if n % i == 0:
                return False
        return True

    prime_number_index = []

    for i in range(len(list)):
        if is_prime(list[i]):
            prime_number_index.append(i)

    print(f"Vị trí các phần tử là số nguyên tố: {prime_number_index}")

def ex7(list):
    print(f"Danh sách: {list}")
    check = []
    for i in list:
        if list.count(i) == 1:
            check.append(i)
    print(f"Các phần tử duy nhất trong danh sách là: {check}")


def ex8(list):
    print(f"Danh sách: {list}")
    unique_numbers = []
    count = []
    for num in list:
        if num not in unique_numbers:
            unique_numbers.append(num)
            count.append(0)
    for i in range(len(unique_numbers)):
        for num in list:
            if num == unique_numbers[i]:
                count[i] += 1

    for i in range(len(unique_numbers)):
        print(f"Giá trị {unique_numbers[i]}: {count[i]} lần")


def ex9(list):
    print(f"Danh sách: {list}")
    subsequences = []
    current_subseq = [list[0]]

    for i in range(1, len(list)):
        if list[i] < list[i - 1]:
            current_subseq.append(list[i])
        else:
            if len(current_subseq) > 1:
                subsequences.append(current_subseq[:])
            current_subseq = [list[i]]

    if len(current_subseq) > 1:
        subsequences.append(current_subseq)

    print("Các đoạn con giảm liên tiếp:")
    for subseq in subsequences:
        print(subseq)

if __name__ == '__main__':
    n = int(input("Nhập số phần tử n trong danh sách: "))
    ds = generate_list(n)
    #ds = [3, 3, 54, 28, 28, 31, 54]
    while True:
        os.system("cls")
        select = menu()
        choice(select, ds)
        os.system("pause")
        if select == 10:
            break

