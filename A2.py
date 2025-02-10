import random
while True:
    print ('Welcome to Rock Paper Scissors!')
    choice = input('Please Enter Your Choice: ')
    possible_choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(possible_choices)
    print (f'You Chose {choice.capitalize()}.')
    print (f'Computer Chose {computer_choice.capitalize()}.')
    if choice.lower() == computer_choice:
        print (f'Both Players Selected {computer_choice.capitalize()}. It\'s a tie!')
    elif choice.lower() == 'rock':
        if computer_choice == 'scissors':
            print ('Rock Smashes Scissors. You Win!')
        else:
            print ('Paper Covers Rock. You Lose!')
    elif choice.lower() == 'paper':
        if computer_choice == 'rock':
            print ('Paper Covers Rock. You Win!')
        else:
            print ('Scissors Cut Paper. You Lose!')
    elif choice.lower() == 'scissors':
        if computer_choice == 'paper':
            print ('Scissors Cut Paper. You Win!')
        else:
            print ('Rock Smashes Scissors. You Lose!')
    else:
        print ('Invalid Input!')
    play_again = input('Do You Want to Play Again? Yes/No: ')
    if play_again != 'Yes':
        break