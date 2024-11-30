import random

def gamer_check_function(gamer_check):
    while True:
        if gamer_check == 'yes':
            break
        elif gamer_check == 'no':
            exit()
        else:
            gamer_check =input('Please type "yes" or "no": ')
            continue
    return

def main():
    computer_guess = random.randrange(1,21)
    counter_guess = 0
    while True:
        user_guess = input('Please enter the number between 1 and 20: ')
        counter_guess = counter_guess+1
        if user_guess == "x":
            exit()
        if user_guess == "n":
            gamer_check = str(input('Do you want to play a new game? Enter "yes" or "no". ' ))
            gamer_check_function(gamer_check)
            counter_guess = 0
            computer_guess = random.randrange(1,21)
            continue 
        if user_guess == "s":
            print(f'The hidden number is {computer_guess}')
            counter_guess = counter_guess-1
            continue
        if computer_guess == int(user_guess):
            print('Your guess is right! The number of guessing attempts:', counter_guess)
            gamer_check = str(input('Do you want to play again? Enter "yes" or "no". ' ))
            gamer_check_function(gamer_check)
            counter_guess = 0
            computer_guess = random.randrange(1,21)
            continue
        elif computer_guess > int(user_guess):
            print('Your guess is too small')
            continue
        elif computer_guess < int(user_guess):
            print('Your guess is too big')
            continue

main()