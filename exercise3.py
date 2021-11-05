# exercise 3
import random


guessed_number=random.randint(1,10)
print(guessed_number)

guess=int(input("Please guess the number: "))

while (guess!=guessed_number):


    if guess<guessed_number:
        print("increase your number")
        guess=int(input("Please enter a new number: "))


    elif guess>guessed_number:
        print("decrease your number")
        guess=int(input("Please enter a new number: "))


    #else:
    print("Congratulations, it is true")


