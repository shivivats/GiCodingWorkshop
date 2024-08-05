# ---- The most basic version of the program ----
import random

number = random.randint(1, 10)

print("I'm thinking of a number between 1 and 10.")

while True: # means the game runs forever (until we break it ourselves)
    print("Guess the number: ")

    guess = input()

    guess = int(guess) # all inputs are "strings", we need to transform the string to an "int" to use it in an integer-basd operation later in the if statement

    # if-else statements are "conditional statements"
    # if CONDITION:
    #     DO THIS
    # else:
    #     DO THAT
    if guess == number: 
        print("Correct! You win!")
        break
    else:
        print("Wrong!")

# -------------------------------------------------------
# The first thing we're gonna do is.. cheat

print("Computer's thinking of the number " + str(number))

# This will help us test our game faster!

# CUSTOMISE IT! CHANGE ANY OF THE STRINGS TO SAY ANYTHING THAT YOU'D LIKE!

# -------------------------------------------------------
# Now what if you wanted to change the range?
# You are going to have to change the random number generation and the string!
# instead, we can use variables!

# --- introduce variables here!
# Copy everything to main.py or just use the shell to run the hitpoints file
# python ./hitpoints/hitpoints.py

# now we can store the two values for the number as variables!

lower=1
upper=10
number=random.randint(lower, upper)

print("I'm thinking of a number between " + str(lower) + " and " + str(upper) + ".")

# CUSTOMISE IT! CHANGE THE NUMBERS TO ANYTHING YOU LIKE!

# ------------------------------------------------------
# Now, what if your game is too difficult?
# We can try to add a way to tell the player if they guessed higher or lower than the computer's number to nudge them in the right direction

# at the end of the while loop
if guess < number:
    print("Try guessing a little higher.")

else:
    print("Try guessing a little lower.")


# ------------------------------------------------------
# Finally, we have to do some checks to make sure the user does not break our game by entering something that is not an integer!
# Even though the we are inputting strings, we had to transform the string to an integer

# after guess = input()

if not guess.isdigit():
    print("Please input in a number!")
    continue

# guess = int(guess)

# We can also add make sure some of our print statements don't go to the new line, just for better reading

print("Guess the number: ", end ="")

print("Wrong!", end=" ")


# ------------------------------------------------------
# We can also tell the player to stay in range if they input something out of range
# But that's homework!
