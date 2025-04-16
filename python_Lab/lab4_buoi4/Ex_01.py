"""
Viết 1 game chgo phép người dùng đoán số từ 1 đến 100.
Game có 3 cấp độ chơi:
    - dễ - đoán tối đa 9 lần
    - vừa - đoán tối đa 6 lần
    - khó - đoán tối đa 4 lần
Sau khi người dùng hoàn tất 1 lần chơi,
    chương trình sẽ hỏi người dùng có chơi nữa không.
    - Nếu người chơi đồng ý thì tiếp tục 1 lần chơi mới.
    - Nếu không thì kết thúc trò chơi, thống kê số lần chơi thắng/thua
"""

import random

def choose_level():
    print(
        "This is the guess number game.\nChoose the level for this game:\n\t1. hard\n\t2. medium\n\t3. easy")
    level = 1
    while True:
        level = int(input("Your selection: "))
        if 1 <= level <= 3:
            break

    return 4 if level == 1 else 6 if level == 2 else 10


def game_action(count):
    is_win = False
    rand_num = int(random.randint(1, 100))
    for i in range(count):
        guess_num = int(input("Guess a number from 1 to 100: "))
        if guess_num == rand_num:
            print(f"Nice! You guessed the number {guess_num}. After {i + 1} time")
            is_win = True
            break
        else:
            if guess_num < rand_num:
                print(f"Your guess is lower than the number. Try again.")
            else:
                print(f"Your guess is higher than the number. Try again.")


    print(f"You lose the game! The number is {rand_num}.")
    return is_win

if __name__ == '__main__':
    no_plays = 0
    no_wins = 0
    while True:
        no_plays += 1
        game_level = choose_level()
        if game_action(game_level):
            no_wins += 1
        select = input("Do you want to play again? (Y/N)").lower()
        if select == 'n':
            break

    print(f"Plays count = {no_plays}")
    print(f"Wins count = {no_wins}")
