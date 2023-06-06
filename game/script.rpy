# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image puzzleRoomWithKey = "bg/Background_With_Key.png"
image puzzleRoomWithoutKey = "bg/Background_Without_Key.png"
image puzzleRoom = "bg/Puzzle_Room.png"

image key = "objects/Key.png"

image wilbur = "characters/wilbur/Professor_Wilbur.png"

define w = Character("Wilbur", color="#c8ffc8")
define inventory = []

transform on_table:
    xpos 790
    ypos 385

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show wilbur

    # These display lines of dialogue.

    w "Hey, Wes!"

    w "This is a great idea!"

    w "We're going to start by building a simple brick in the form of a puzzle."

    w "Once we have that, it's just a matter of stacking bricks on top of each other."

    w "We'll get there in no time."

    w "So, let's begin the puzzle..."

    jump puzzle

    # This ends the game.

    return

label puzzle:
    scene puzzleRoom

    show key at on_table

    w "On the table in front of you is a key."

    w "On the other side of the room is a door."

    w "For whatever reason, you feel compelled to leave this room."

    call loop

    w "Congratulations! You solved the puzzle!"

    w "Now, let's make it better!"

    return

label loop:
    menu:
        w "What would you like to do?"

        "Take the key" if not 'key' in inventory:
            hide key
            $ inventory.append('key')
            w "You take the key off the table! Maybe it will fit the door?"
            call loop
        "Try and turn the handle":
            w "You try to jiggle the knob. But, unfortunately, the door is locked..."
            call loop
        "Unlock the door" if 'key' in inventory:
            w "You slide the key into the door! It opens! You leave the room!"
            return
