import random

lower=1
upper=10
number=random.randint(lower, upper)

print("Computer's thinking of the number " + str(number))

print("I'm thinking of a number between " + str(lower) + " and " + str(upper) + ".")

while True:
    print("Guess the number: ", end ="")

    guess= input()

    if not guess.isdigit():
        print("Please input in a number!")
        continue

    guess = int(guess)

    if guess == number:
        print("Correct! You win!")
        break

    print("Wrong!", end=" ")

    if guess < number:
        print("Try guessing a little higher.")

    else:
        print("Try guessing a little lower.")


