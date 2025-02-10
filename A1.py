import random
num = str(random.randint(1, 10))
tries = 0
print ('I will generate a number from 1 to 10. The game ends when you guess the number correctly.')
while True:
    guess = input('Enter Your Guess: ')
    tries += 1
    if guess == num:
        print ('You Win!')
        print ('Tries:', tries)
        break
    else:
        print ('That\'s not the number. Try again!')