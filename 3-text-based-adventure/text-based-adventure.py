# TODO:
# make the invalid choice into a function too
# make the invalid choice more consistent
# make the game start again after an invalid choice
# make each "room" into a class and use functions to show the text
# ask the user for their name at the beginning and display that name
# add the "short versions" of the prompts to the if statements as well so we have other options for the user


def fleeText():
  print("Scared from the growls coming from the cave, you fled back on the path through the woods, where Silas and Brangar await you.")
  print("You can already imagine their disappointed faces when you'll share this news with them.")
  print("The end.")


def winText():
  print("You carry Gundren out of the cave without anyone else noticing and make your way back to Silas and Brangar, awaiting the relief on their faces when they see their companion brought back safely.")
  print("The end.")

# The idea is to describe situations, take user input and describe what happens
# Do this in a loop and eventually end the game

import random

# Ask the player for their name
print("What is your name?")
player_name = input("> ")

# Print a welcome message
print("Welcome to Cragmaw Hideout, " + player_name + ".....")

# Cave Mouth
print("Following a forest trail, you come across a large cave in a hillside.")
print("A shallow stream flows out of the cave mouth, which is screened by dense shrubs.")
print("A narrow dry path leads into the cave on the right-hand side of the stream.")
print("Would you like to go towards the cave or flee?")

# Wait for user input
entrance_choice = input("> ")

# Do something based on the user's input
if entrance_choice == "go towards the cave": # or entrance_choice == "go towards"
  print("As you approach the cave, you notice a small area in the shrubs on the east side of the stream has been hollowed out to form a lookout.")
  print("Wooden planks flatten out the shrubs and provide room for guards to lie hidden and watch the area—including a pair of goblins lurking there right now!")
  print("Would you like to go into the cave, try to ambush the goblins, or flee?")

  # print("You see a room with two wolves leashed inside it. They are yanking their chains trying to reach a figure tied up in the corner, but the leashes are letting the person survive.... for now")
  # print("By the mark on their clothes, you can identify the prisoner as Gundren Rockseeker, the person you were sent here to rescue.")
  # print("You can walk around the wolves and try to flee Gundren, distract the wolves with food and try to free Gundren, or you can still flee.")
  # print("What would you like to do?")

  thicket_choice = input("> ")
  if thicket_choice == "go into the cave":
    # stealthRoll = random.randint(1, 20)
    # if stealthRoll > 10):
    #   print("You sneak into the cave mouth without the goblins noticing you.")
    # else:
    #   print("The goblins spot you, you are dead.")
    print("The goblins spot you and fire their arrows.")
    print("One of them finds its mark, you are dead.")
    print("The end.")

  elif thicket_choice == "ambush the goblins":
    print("You sneak around the goblins and quickly shoot two arrows at them.")
    print("Unaware of your presence, they have no time to react and are quickly felled.")

    print("Would you like to go into the cave?")
    cave_choice = input("> ")

    if cave_choice == "yes": # or cave_choice == "go into the cave"
      print("Just inside the cave mouth, a few uneven stone steps lead up to a small, dank chamber on the east side of the passage.")
      print("The cave narrows to a steep fissure at the far end, and is filled with the stench of animals.")
      print("Savage snarls and the sounds of rattling chains greet your ears where three wolves are chained up just inside the opening.")
      print("Each wolf's chain leads to an iron rod driven into the base of a stalagmite.")
      print("They are yanking their chains trying to reach a figure tied up in the corner, but the leashes are letting the person survive.... for now")
      print("By the mark on their clothes, you can identify the prisoner as Gundren Rockseeker, the person you were sent here to rescue.")
      print("You can walk around the wolves and try to flee Gundren, distract the wolves with food and try to free Gundren, or you can still flee.")
      print("What would you like to do?")

      gundren_choice = input("> ")
      if gundren_choice == "walk around the wolves": # or cave_choice == "walk around"
        print("You successfully walk around the wolves and manage to free Gundren.")
        winText()

      elif gundren_choice == "distract the wolves with food": # or cave_choice == "distract" or cave_choice = "distract with food"
        print("You throw some of your rations at the wolves. The seemingly starved animals quickly leap to grab and begin to devour it.")
        print("You use this distraction and quickly make your way to Gundren, freeing him.")
        winText()

      elif gundren_choice == "flee":
        fleeText()

      else:
        print("Invalid choice!.")

    else:
      fleeText()

  else:
    fleeText()

elif entrance_choice == "flee":
  fleeText()

else:
  print("Invalid choice!.")


