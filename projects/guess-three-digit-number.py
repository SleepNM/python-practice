'''
Try to guess randomly generated 3 digit number.
'''

import random


def create_hidden():
    hidden = ""
    digits = list(range(10))
    random.shuffle(digits)
    numb = digits[:3]
    for num in numb:
        hidden += str(num)
    return hidden


def check_numbers(guess, number):
    if guess[0] == number[0] or guess[1] == number[1] or guess[2] == number[2]:
        print("Match")
        return True
    elif guess[0] == number[1] or guess[0] == number[2] or\
        guess[1] == number[0] or guess[1] == number[2] or\
            guess[2] == number[0] or guess[2] == number[1]:
        print("Close")
        return True
    else:
        print("Nope")
        return True


def check_win(guess, number):
    global play
    if guess == number:
        print("Congratulations, You have Won!!!")
        play = False
    else:
        pass


def ask_for_guess():
    global user_guess
    while True:
        user_guess = str(input("What is your guess? "))
        if len(user_guess) != 3:
            print("Enter a three digit number")
            continue
        else:
            break


hidden_number = create_hidden()
play = True


while play:
    ask_for_guess()
    check_win(user_guess, hidden_number)
    check_numbers(user_guess, hidden_number)
