import random

# generate 3 digit number
num1 = str(random.randrange(9))
num2 = str(random.randrange(9))
num3 = str(random.randrange(9))

code = num1 + num2 + num3

print(code)

correct = False

while correct is False:

    guess = input("Enter a guess:")

    if guess == code:
        print("correct")
        correct = True

    elif guess > code:
        print("too high! try again")

    elif guess < code:
        print("too low! try again")
