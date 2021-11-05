# exercise 1
def sum_odd_number(N):
    sum= 0
    for n in range(1, N+1):
        if (n & 2!=0):
            #print("debug odd" ,n)
            sum= sum + n
     return sum

def avg_even_number(N):
    sum= 0
    for n in range(1, N+1):
        if (n % 2==0)
            #print("debug even", n)
            sum= sum + n
    return sum/N

i=int(input("Please enter a number:"))
print("first calculation", sum_odd_number(i))
print("second calculation", avg_even_number(i))

# exercise 2
def email_check(string):
    for letter in string:
        if '@' and '.' in string:
            return True
        else:
            return False

email=input("Enter your e-mail: ")
print("This email is",email_check(email))

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
