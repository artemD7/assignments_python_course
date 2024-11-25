import random


game_counter = 0
while True:
    if  game_counter > 0:
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
                    counter_guess = counter_guess-1
                    gamer_check_2 = str(input('Do you want to play a new game? Enter "yes" or "no". ' ))
                    if gamer_check_2 == 'yes':
                        game_counter = 0
                        break
                    elif gamer_check_2 == 'no':
                        exit()
                    else:
                        print('After pressing "n", please type "yes" or "no"')
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
            print('The number of guessing attempts: ', counter_guess)
        elif gamer_check == 'no':
            break
        else:
            print("Please type the right answer")
            continue
    else:
        computer_guess = random.randrange(1,21)
        counter_guess = 0
        game_counter = game_counter + 1
        while True:
            user_guess = input('Please enter the number between 1 and 20: ')
            counter_guess = counter_guess+1
            if user_guess == "x":
                exit()
            if user_guess == "n":
                counter_guess = counter_guess-1
                gamer_check_2 = str(input('Do you want to play a new game? Enter "yes" or "no". ' ))
                if gamer_check_2 == 'yes':
                    game_counter = 0
                    break
                elif gamer_check_2 == 'no':
                    exit()
                else:
                    print('After pressing "n", please type "yes" or "no"')
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
        print('The number of guessing attempts: ', counter_guess)
        continue
