import random

"""
1. Write a program that prints numbers from 1 to 10
"""
def ex_01():
    for i in range(1, 11):
        print(i)



"""
2. Write a program to calculate the sum of numbers in a range from 1 to n (n is entered from the keyboard)
"""
def ex_02():
    n = int(input("Enter the range: "))
    sum = 0
    for i in range(1, n+1):
        sum = (n * (n+1))/2
    print(f"The sum of numbers in a range from 1 to {n}: {sum}")



"""
3. Write a program to calculate the sum of even (/odd) numbers in a range from 1 to n (n is entered from the keyboard)
"""
def ex_03():
    n = int(input("Enter the range: "))
    sum_even = 0
    sum_odd = 0
    for i in range(1, n+1):
        if i%2==0:
            sum_even += i
        else:
            sum_odd += i

    print(f"The sum of even numbers in a range from 1 to {n}: {sum_even}")
    print(f"The sum of odd numbers in a range from 1 to {n}: {sum_odd}")



"""
4. Write a program to check how many vowels are in a string entered from the keyboard.
"""
def ex_04():
    string = input("Enter the string: ")
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in string.lower():
        if char in vowels:
            count += 1
    print(f"There are {count} vowels in the string.")



"""
5. Write a program to count the number of words in a sentence the user enters.
"""
def ex_05():
    sentence = input("Enter the sentence: ")
    count = 1
    for word in sentence:
        if word == ' ':
            count += 1
    print(f"There are {count} words in the sentence: {sentence}")



"""
6. Write a program that implements a game as the following description:
	1. The computer generates a random number from 1 to 100
	2. The user was asked to guess
	3. match the user-guessing number to the generated number
	
	You are asked for enhancing this game by giving the level for selection. 
        hard: 4 times, 
        medium: 6 times, 
        easy: 10 times
"""
def ex_06():
    def choose_level():
        print("This is the guess number game.\nChoose the level for this game:\n\t1. hard\n\t2. medium\n\t3. easy\n\t4. exit")
        level = 1
        while True:
            level = int(input("Your selection: "))
            if 1 <= level <= 3:
                break

        return 10 if level == 1 else 6 if level == 2 else 4


    def game_action(count):
        is_win = False
        rand_num = int(random.randint(1, 100))
        for i in range(count):
            guess_num = int(input("Guess a number from 1 to 100: "))
            if guess_num == rand_num:
                print(f"Nice! You guessed the number {guess_num}. After {i+1} time")
                is_win = True
                break
            else:
                if guess_num < rand_num:
                    print(f"Your guess is lower than the number. Try again.")
                else:
                    print(f"Your guess is higher than the number. Try again.")

                print(f"You lose the game! The number is {rand_num}.")
                return is_win

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



if __name__ == '__main__':
    #ex_01()
    #ex_02()
    # ex_03()
    # ex_04()
    # ex_05()
     ex_06()