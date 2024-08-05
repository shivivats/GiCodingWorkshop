import random

lower=1
upper=10
computer_number=random.randint(lower, upper)

# comment this line out if you don't wanna cheat!
print("Computer's thinking of the number " + str(computer_number))

print("I'm thinking of a number between " + str(lower) + " and " + str(upper) + ".")

guess = 0

while guess != computer_number:
    
    print("Guess the number: ", end ="")

    guess= input()

    if guess.isdigit():
        guess = int(guess)

        if guess == computer_number:
            print("Correct! You win!")
        
        else:
            
            print("Wrong!", end=" ")

            if guess < computer_number:
                print("Try guessing a little higher.")

            else:
                print("Try guessing a little lower.")

    else:
        print("Please input a number!")
