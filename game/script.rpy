# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image puzzleRoom = "rooms/Puzzle_Room.png"

define e = Character("Eileen")

default in_room = False
default move_count = 0
default current_room = "PuzzleRoom"
default previous_room = ""

define inventory = []
define mirror_placed = False

# The game starts here.

label start:
    e "Here is the start of your game."

    #Call the first scene
    $ current_room = "PuzzleRoom"
    call MyRoom

    e "You finished the game!"

    return

label MyRoom:
    #Update values behind the scenes
    $ update_gamestate()

    #Enter the scene
    $ in_room = False
    $ renpy.show_screen(current_room + "Screen")

    #React to entrance
    if current_room != previous_room:
        $ check_intro_reactions(current_room)
    $ previous_room = current_room

    #Enable scene interactivity
    $ in_room = True
    $ renpy.call_screen(current_room + "Screen")

    return

label Hammer:
    $ renpy.show_screen(current_room + "Screen")

    e "On the table in the puzzle room, there's a hammer."

    e "It's shimmering. Even the wooden handle, which is odd."

    e "Pick it up?"

    menu:
        "Pick up the hammer":
            jump TakeHammer
        "Leave the hammer where it is":
            jump LeaveHammer
    jump MyRoom

label Mirror:
    $ renpy.show_screen(current_room + "Screen")

    e "Against the wall of the puzzle room, there's a mirror."

    e "Interestingly, you don't see your reflection in it... Maybe you're a vampire!"

    e "Pick it up?"

    menu:
        "Pick up the mirror":
            jump TakeMirror
        "Leave the mirror where it is":
            jump LeaveMirror
    jump MyRoom

label TakeMirror:
    $ inventory.append('mirror')

    e "The mirror is now in your inventory!"

    jump MyRoom

label LeaveMirror:
    e "You leave the mirror where it is."

    jump MyRoom

label TakeHammer:
    $ inventory.append('hammer')

    e "The hammer is now in your inventory!"

    jump MyRoom

label LeaveHammer:
    e "You leave the hammer where it is."

    jump MyRoom

label EndGame:
    e "Let's finish the game!"

    return

label LookAtDinner:

    $ in_room = False

    $ renpy.show_screen(current_room + "Screen")

    e "Oooh! Looks like we're having pizza!"

    jump MyRoom

label EnterPuzzleRoom:
    e "I just entered the puzzle room!"

    return

label EnterDiningRoom:
    e "I just entered the dining room!"

    return
