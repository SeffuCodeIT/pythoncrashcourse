# 1.the computer will generate a random numer
# 2.you need to guess a number
# 3.feedback is based on your input
# 4.if you guess more than six times then you lose
print("lets get started")
import random

guesses_taken = 0

guess_number = random.randint(0,10)

while guesses_taken < 6:
    print('take a guess')
    my_num = input()
    my_num = int(my_num)

    guesses_taken = guesses_taken+1

    if my_num < guess_number:
        print('your number is too low')
    
    if my_num > guess_number:
        print("youre number is too high")
    
    if my_num == guess_number:
        break

if my_num == guess_number:
    guesses_taken = str(guesses_taken)
    print('Good job, ' + '! You guessed my number in ' + guesses_taken + ' guesses!')

if guesses_taken != guess_number:
    guess_number = str(guess_number)
    print('The number I was thinking of was ' + str(my_num))









# guess_number = random.randint(0,10)
# my_num = input()

# if my_num == guess_number:
#     print("you've won")
# else:
#     print("you lost")

