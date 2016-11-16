print("Welcome to LoveGreg")
playerName=input("What is your name?")
print("Welcome to LoveGreg, live or die "+playerName)

print("""Chapter 01
You are in the basement of a pub in Winterhold.
You and your friends are massively hung over.

You wake up and see broken pool cue.
To your left you see two doors and to your right you see the stairs.""")

done = False
verbs = ["open", "look", "climb", "grab", "take", "fight"]
nouns = ["stairs", "door", "friends", "cue", "goblins"]
# to do: handle multi word nouns
cueOwnership = False
while not done:
    action = ""
    thing = ""

    command = input(">>> ")
    words = command.split()
    for word in words:
        if word in verbs:
            action = word
        if word in nouns:
            thing = word
    print(action+"ing" + " " + thing )
    if action == "climb" and thing == "stairs":
        print(playerName + " trips and dies")
        done = True
    if action == "open" and thing == "door":
        print("You open a door and goblins assult you. Prepare to fight.")
    if action == "fight" and thing == "goblins":
        if not cueOwnership:
            print("Sorry "+playerName+", you have nothing to fight with and die.")
            done = True
        if cueOwnership:
            print("you got 99 problins but a goblin aint one!!! treasure chest")
            done = True
    if (action == "grab" or action == "take") and thing == "cue":
        print("it's your cue :)")
        cueOwnership = True
