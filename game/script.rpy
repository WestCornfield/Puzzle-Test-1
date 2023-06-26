# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

default in_room = False
default move_count = 0
default current_room = "PuzzleRoom"
default previous_room = ""

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
