"""
Viết 1 game Tài xỉu dưa trên nguyên tắc gieo 2 con xúc sắc ngẫu nhiên.
Nếu tổng giá trị của 2 con xúc sắc > 5, gọi là "Tài"
Còn không, gọi là "Xỉu"

Cho người dùng chọn 1 trong 2 trạng thái Tài hoặc Xỉu.
So sánh kết quả.
Hỏi người chơi có tiếp tục không? Nếu có thì chơi tiếp cho dến khi người dùng chọn không.

Mở rộng:
    1. Bắt đầu chơi, cho người dùng 1 số tiền là 100,000. Số tiền cược của mỗi lần chơi
        là 10,000. Sau khi người dùng chọn không chơi tiếp hoặc hết tiền thì ngưng. Sau đó thống kê
        tiền của người chơi, số ván thắng. (có thể cho người dùng chọn số tiền đặt cược)
    2. Cho phép người dùng cược vào số 5 (3 trạng thái thay vì 2 (Tài/Xỉu). Nếu người dùng cược đúng
        thì thắng được 3 lần số tiền cược.
"""

import random

def start_game():
    print("Chào mừng bạn đến với trò chơi Tài Xỉu")
    money = 100000
    print(f"Số tiền hiện tại là {money:,}")
    print()

    bet = int(input("Nhập số tiền bạn muốn cược: "))
    while True:
        if bet <= money:
            break
    return money, bet

def game_action(money, bet):
    is_win = False
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    sum_dice = dice1 + dice2

    start_game()

    select = int(input("Mời bạn lựa chọn Tài (1) hay Xỉu (0) hoặc Huề (2): "))
    while True:
        if 0<=select<=2:
            break

    if sum_dice > 5:
        if select == 1:
            money += bet
            print(f"Bạn thắng. Kết quả là {sum_dice}")
            print(f"Số tiền hiện tại là {money}")
        else:
            money -= bet
            print(f"Bạn thua. Kết quả là {sum_dice}")
            print(f"Số tiền hiện tại là {money}")

    elif sum_dice == 5:
        if select == 2:
            money += bet*3
        else:
            money -= bet
            print(f"Bạn thua. Kết quả là {sum_dice}")
            print(f"Số tiền hiện tại là {money}")

    else:
        if select == 0:
            money += bet
            print(f"Bạn thắng. Kết quả là {sum_dice}")
            print(f"Số tiền hiện tại là {money}")
        else:
            money -= bet
            print(f"Bạn thua. Kết quả là {sum_dice}")
            print(f"Số tiền hiện tại là {money}")


if __name__ == '__main__':
    pass