# A variable has a name, a type, and a value
# Name: hitPoints
# Type: integer
# Value: 20

# In most languages you would write "int hitPoints = 20"
# Python is unique in the way we write things, since variables dont always have types
# Thus, we don't need to define a type, and most of the times you do not, but we will do it for the sake of the tutorial
hitPoints : int = 20

# Tell me your hit points
print("Current hit points are: " + str(hitPoints))

input("Press enter to continue...\n")

# Take 10 damage!
print("Taking 10 damage!!")
hitPoints = hitPoints - 10

# How many hit points do you have after taking damage?
print("Current hit points are: " + str(hitPoints))

input("Press enter to continue...\n")

# Are you still alive?
if hitPoints > 0:
    print("You are still alive")

else:
    print("You are dead")


# Heal yourself for half your hit points
input("Press enter to continue...\n")

print("Healing for half the hit points.")

hitPoints = hitPoints + int(hitPoints/2)

print("Current hit points are: " + str(hitPoints))

# ------------------
# What if we took more damage?
input("Press enter to continue...\n")

print("Taking even more damage!")
hitPoints = hitPoints - 20
# we can even clamp this to ensure the HP doesn't go below 0
# we can even check pre-emptively if the damage we take is gonna be more than our hp, then we die anyway

# Check for everything again
print("Current hit points are: " + str(hitPoints))

# Are you still alive?
if hitPoints > 0:
    print("You are alive")

else:
    print("You are dead")