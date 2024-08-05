# Note: There are many ways to do this! And certainly this is not the best one. But it is simple, thus we are doing it.

# Ask the player for their name
print("What is your name?")
player_name = input("> ")

# Print a welcome message
print("Welcome to Cragmaw Hideout, " + player_name + ".....")

# possible locations: cave_mouth, thicket, cave_entrance, gundren_room, flee, win, end
current_location="cave_mouth"

while current_location != "end": # or while True
    if current_location == "cave_mouth":
        print("Following a forest trail, you come across a large cave in a hillside.")
        print("A shallow stream flows out of the cave mouth, which is screened by dense shrubs.")
        print("A narrow dry path leads into the cave on the right-hand side of the stream.")
        print("Would you like to go towards the cave or flee?")

        # Wait for user input
        entrance_choice = input("> ")

        if entrance_choice == "go towards the cave": # or entrance_choice == "go towards"
            current_location = "thicket"
        elif entrance_choice == "flee":
            current_location = "flee"
        else:
            print("Invalid input! Go again!!\n")

    elif current_location == "thicket":
        print("As you approach the cave, you notice a small area in the shrubs on the east side of the stream has been hollowed out to form a lookout.")
        print("Wooden planks flatten out the shrubs and provide room for guards to lie hidden and watch the area—including a pair of goblins lurking there right now!")
        print("Would you like to go into the cave, try to ambush the goblins, or flee?")

        thicket_choice = input("> ")
        if thicket_choice == "go into the cave":
            print("The goblins spot you and fire their arrows.")
            print("One of them finds its mark, you are dead.")
            print("The end.")
            current_location = "end"

        elif thicket_choice == "ambush the goblins":
            print("You sneak around the goblins and quickly shoot two arrows at them.")
            print("Unaware of your presence, they have no time to react and are quickly felled.") 
            current_location = "cave_entrance"
        elif thicket_choice == "flee":
            current_location = "flee"
        else:
            print("Invalid input! Go again!!\n")

    elif current_location == "cave_entrance":
        print("You find yourself at the entrance of the cave, growls can be heard from the inside.")
        print("Would you like to go into the cave?")
        cave_choice = input("> ")

        if cave_choice == "yes":
            current_location = "gundren_room"
        elif cave_choice == "no" or cave_choice == "flee":
            current_location = "flee"
        else:
            print("Invalid input! Go again!!\n")

    elif current_location == "gundren_room":
        print("Just inside the cave mouth, a few uneven stone steps lead up to a small, dank chamber on the east side of the passage.")
        print("The cave narrows to a steep fissure at the far end, and is filled with the stench of animals.")
        print("Savage snarls and the sounds of rattling chains greet your ears where three wolves are chained up just inside the opening.")
        print("Each wolf's chain leads to an iron rod driven into the base of a stalagmite.")
        print("They are yanking their chains trying to reach a figure tied up in the corner, but the leashes are letting the person survive.... for now")
        print("By the mark on their clothes, you can identify the prisoner as Gundren Rockseeker, the person you were sent here to rescue.")
        print("You can walk around the wolves and try to free Gundren, distract the wolves with food and try to free Gundren, or you can still flee.")
        print("What would you like to do?")

        gundren_choice = input("> ")

        if gundren_choice == "walk around the wolves": # or cave_choice == "walk around"
            print("You successfully walk around the wolves and manage to free Gundren.")
            current_location = "win"

        elif gundren_choice == "distract the wolves with food": # or cave_choice == "distract" or cave_choice = "distract with food"
            print("You throw some of your rations at the wolves. The seemingly starved animals quickly leap to grab and begin to devour it.")
            print("You use this distraction and quickly make your way to Gundren, freeing him.")
            current_location = "win"

        elif gundren_choice == "flee":
            current_location = "flee"

        else:
            print("Invalid input! Go again!!\n")

    elif current_location == "flee":
        print("Scared from the growls coming from the cave, you fled back on the path through the woods, where Silas and Brangar await you.")
        print("You can already imagine their disappointed faces when you'll share this news with them.")
        print("The end.")
        current_location = "end"

    elif current_location == "win":
        print("You carry Gundren out of the cave without anyone else noticing and make your way back to Silas and Brangar, awaiting the relief on their faces when they see their companion brought back safely.")
        print("The end.")
        current_location = "end"

    else:
        print("Invalid location!! This should not happen. Check your code.")
