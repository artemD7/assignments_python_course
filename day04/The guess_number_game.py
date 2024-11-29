import random
#let's define the function which reacts on user entering "n"  
def user_press_n():
    while True:
        gamer_check_2 = str(input('Do you want to play a new game? Enter "yes" or "no". ' ))
        if gamer_check_2 == 'yes':
            break
        elif gamer_check_2 == 'no':
            exit()
        else:
            print('Please type "yes" or "no"')
            continue
    return   
# this function works when the user plays second or more game in a row and contains
# user_press_n function
def second_game_and_more():
    gamer_check = str(input('Do you want to play again? Enter "yes" or "no". ' ))
    if gamer_check == 'yes':
        computer_guess = random.randrange(1,21)
        counter_guess = 0
        while True:
            user_guess = input('Please enter the number between 1 and 20: ')
            counter_guess = counter_guess+1
            if user_guess == "x":
                exit()
            if user_guess == "n":
                user_press_n()
                counter_guess = 0
                computer_guess = random.randrange(1,21)
                continue
            if user_guess == "s":
                print(f'The hidden number is {computer_guess}')
                counter_guess = counter_guess-1
                continue
            if computer_guess == int(user_guess):
                print('Your quess is right!') 
                break
            elif computer_guess > int(user_guess):
                print('Your quess is too small')
                continue
            elif computer_guess < int(user_guess):
                print('Your quess is too big')
                continue
        print('The number of guessing attempts:', counter_guess)
    elif gamer_check == 'no':
        exit()
    else:
        print("Please type the right answer")
        return

# the function is reponsible for the very first game of the user in the sequence 
# of games and contains user_press_n function
def first_game(game_counter):
    computer_guess = random.randrange(1,21)
    counter_guess = 0
    game_counter = game_counter + 1
    while True:
        user_guess = input('Please enter the number between 1 and 20: ')
        counter_guess = counter_guess+1
        if user_guess == "x":
            exit()
        if user_guess == "n":
            user_press_n()
            counter_guess = 0
            computer_guess = random.randrange(1,21)
            continue 
        if user_guess == "s":
            print(f'The hidden number is {computer_guess}')
            counter_guess = counter_guess-1
            continue
        if computer_guess == int(user_guess):
            print('Your quess is right!') 
            break
        elif computer_guess > int(user_guess):
            print('Your quess is too small')
            continue
        elif computer_guess < int(user_guess):
            print('Your quess is too big')
            continue
    print('The number of guessing attempts:', counter_guess)
    return game_counter
# this is the main function which operates with second_game_and_more and 
# first_game function
def main(game_counter):
    while True:
        if  game_counter > 0:
            second_game_and_more()
        else:
            game_counter = first_game(game_counter)
# here we do the functions call
game_counter = 0
main(game_counter)