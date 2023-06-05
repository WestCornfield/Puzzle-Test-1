# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen", color="#c8ffc8")
define inventory = []

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "Hey, Wes!"

    e "This is a great idea!"

    e "We're going to start by building a simple brick in the form of a puzzle."

    e "Once we have that, it's just a matter of stacking bricks on top of each other."

    e "We'll get there in no time."

    e "So, let's begin the puzzle..."

    call puzzle

    # This ends the game.

    return

label puzzle:
    e "On the table in front of you is a key."

    e "On the other side of the room is a door."

    e "For whatever reason, you feel compelled to leave this room."

    call loop

    e "Congratulations! You solved the puzzle!"

    e "Now, let's make it better!"

    return

label loop:
    menu:
        e "What would you like to do?"

        "Take the key" if not 'key' in inventory:
            $ inventory.append('key')
            e "You take the key off the table! Maybe it will fit the door?"
            call loop
        "Try and turn the handle":
            e "You try to jiggle the knob. But, unfortunately, the door is locked..."
            call loop
        "Unlock the door" if 'key' in inventory:
            e "You slide the key into the door! It opens! You leave the room!"
            return
