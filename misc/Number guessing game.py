import random

n=random.randint(0, 99)
print('The random number is between 0 and 99')

no_of_guess=0
while no_of_guess < 10000:
    y=int(input('Enter your guess :' ))
    no_of_guess += 1

    if y < n :
        print('the guess is low')

    elif y > n :
        print('the guess is high')

    elif y==n:
        break

if y==n:
    print('You guessed the number in ' + str(no_of_guess) + ' tries!')

else:
    print('You did not guess the number, The number was ' + str(n)) 
    