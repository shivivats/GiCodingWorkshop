def fleeText():
  print("Scared from the growls, you fled back on the path through the woods, where Silas and Brangar await you.")
  print("You can already imagine their disappointed faces as you'll share this with them")
  print("The end.")


def winText():
  print("You carry him out of the cave without anyone else noticing and make your way back to Silas and Brangar, awaiting the relief on their faces when they see their companion brought back safely.")
  print("The end")

# The idea is to describe situations, take user input and describe what happens
# Do this in a loop and eventually end the game

# Print a welcome message
print("You see a cave in front of you. Moss grows on the rocky entrance, and sounds of running water and animal growls can be heard from the inside.")
print("You see a wooden path disappear into the cave. Your vision is limited to a few meters.")
print("Would you like to explore the cave or flee?")

# Wait for user input
userChoice = input("> ")

# Do something based on the user's input
if(userChoice == "explore the cave"): # or userChoice == "explore"
  print("Some text here about the river and other visual descriptions of the cave...")
  print("You see a room with two wolves leashed inside it. They are yanking their chains trying to reach a figure tied up in the corner, but the leashes are letting the person survive.... for now")
  print("By the mark on their clothes, you can identify the prisoner as Gundren Rockseeker, the person you were sent here to rescue.")
  print("You can walk around the wolves and try to flee Gundren, distract the wolves with food and try to free Gundren, or you can still flee.")
  print("What would you like to do?")

  caveChoice = input("> ")

  if(caveChoice == "walk around the wolves"): # or caveChoice == "walk around"
    print("You successfully walk around the wolves and manage to free Gundren.")
    winText()

  elif(caveChoice == "distract the wolves with food"): # or caveChoice == "distract" or caveChoice = "distract with food"
    print("You throw some of your rations at the wolves. The seemingly starved animals quickly leap to grab and begin to devour it.")
    print("The wolves take a liking to you and let you walk across the chamber and free Gundren.")
    winText()

  elif(caveChoice == "flee"):
    fleeText()

  else:
    print("Invalid choice! Please enter one of the choices described above.")


elif(userChoice == "flee"):
  fleeText()


else:
  print("Invalid choice! Please enter one of the choices described above.")


# TODO:
# make the invalid choice into a function too
# make the game start again after an invalid choice
# make each "room" into a class and use functions to show the text
# ask the user for their name at the beginning and display that name
# add the "short versions" of the prompts to the if statements as well so we have other options for the user