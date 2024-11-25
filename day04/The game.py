import random
game_counter = 0
while True:
    if  game_counter > 0:
        gamer_check = str(input('Do you want to play more? Enter "yes" or "no". ' ))
        if gamer_check == 'yes':
            computer_guess = random.randrange(1,21)
            counter_guess = 0
            while True:
                user_guess = int(input('Please enter the number between 1 and 20: '))
                counter_guess = counter_guess+1
                if computer_guess == user_guess:
                    print('Your quess is right!') 
                    break
                elif computer_guess > user_guess:
                    print('Your quess is too small')
                    continue
                elif computer_guess < user_guess:
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
            user_guess = int(input('Please enter the number between 1 and 20: '))
            counter_guess = counter_guess+1
            if computer_guess == user_guess:
                print('Your quess is right!') 
                break
            elif computer_guess > user_guess:
                print('Your quess is too small')
                continue
            elif computer_guess < user_guess:
                print('Your quess is too big')
                continue
        print('The number of guessing attempts: ', counter_guess)
        continue
