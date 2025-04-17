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

def roll_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    return dice1, dice2, total

def dice_result(total):
    if total < 5:
        return "Xỉu"
    elif total == 5:
        return "Huề"
    else:
        return "Tài"

def get_bet(current_money):
    while True:
        bet = int(input("Nhập số tiền bạn muốn cược (10,000 trở lên): "))
        if bet > current_money:
            print("Tiền cược vượt quá số dư")
        elif bet < 10000:
            print("Số tiền phải lớn hơn 10,000")
        else:
            return bet

def get_choice():
    while True:
        choice = int(input("Mời bạn lựa chọn Tài (1) hay Xỉu (0) hoặc Huề (2): "))
        if choice == 1:
            return "Tài"
        elif choice == 0:
            return "Xỉu"
        elif choice == 2:
            return "Huề"
        else:
            print("Lựa chọn không hợp lệ")


def game_action():
    money = 100000
    no_plays, no_wins = 0, 0

    while money > 10000:
        print(f"Số tiền hiện tại là {money:,}")
        choice = get_choice()
        bet = get_bet(money)

        dice1, dice2, total = roll_dice()
        result = dice_result(total)

        print(f"Kết quả của trò chơi là: {dice1} + {dice2} = {total} => {result}")
        no_plays += 1
        if choice.lower() == result.lower():
            if result == "Huề":
                winning_money = bet*3
                print(f"Chúc mừng bạn đã thắng {winning_money} (tiền cược gấp 3 lần)")
            else:
                winning_money = bet
                print(f"Chúc mừng bạn đã thắng {winning_money}")
            money += winning_money
            no_wins += 1
            print(f"Số tiền hiện tại: {money:,}")
        else:
            print(f"Rất tiếc bạn đã mất {bet}")
            money -= bet
            print(f"Số tiền hiện tại: {money:,}")
            print()

        if money < 10000:
            print("Bạn không đủ tiền để tham gia")
            print()
            break

        while True:
            play_again = input("Bạn có muốn chơi tiếp không (Y/N)?").lower()
            if play_again in ["y", "n"]:
                break
            print("Nhập 'Y' hoặc 'N' giúp tôi.")
        if play_again == "n":
            break


    print("Trò chơi kết thúc!")
    print(f"Số lượt chơi: {no_plays}")
    print(f"Số lượt thắng: {no_wins}")
    print(f"Số tiền còn lại: {money}")

if __name__ == '__main__':
    print("Chào mừng bạn đến với trò chơi Tài Xỉu")
    game_action()


