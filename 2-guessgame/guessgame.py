import random

lower = 1
upper = 100

computer_number = random.randint(lower, upper)
#computer_number = 5

print("Computer's thinking of " + str(computer_number))

print("I'm thinking of a number between " + str(lower) + " and " + str(upper))

guess = 0

counter = 0

maxGuesses = 5

print("You have " + str(maxGuesses) + " guesses!")

# Loop runs while user guess is NOT EQUAL to computer_number and while the user has made less than 5 guesses
while guess != computer_number and counter < maxGuesses:
    
    # 1. User inputs a number
    guess = input("Guess a number: ")
    
    if guess.isdigit(): # check if the guess is a number made of digits
        guess = int(guess)
    
        # check for whether the user entered a number within the range
        if guess > upper or guess < lower:
            print("Enter a number within the range")
        else:
            # 2. Check the number against the computer_number
            if guess == computer_number:
                print("Correct! You win!") # 3. Show the player some feedback text
            else:
                print("Wrong!")
                # Check if user guess is greater or lower
                if guess > computer_number:
                    print("Try guessing lower!")
                else:
                    print("Try guessing higher!")
    else:
        print("Please input a digit!")
        
    counter = counter + 1


print("Thanks for playing!")
