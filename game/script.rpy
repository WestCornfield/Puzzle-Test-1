# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image puzzleRoom = "rooms/Puzzle_Room.png"

define e = Character("Eileen")

default in_room = False
default move_count = 0
default current_room = "PuzzleRoom"
default previous_room = ""

define audio.rock_smash = "audio/sounds/rock_smash.mp3"
define audio.stone_slide = "audio/sounds/stone_slide.mp3"

define inventory = []
define inside_option = False
define mirror_placed = False
define wall_smashed = False
define scroll_read = False

define open_menu = False
define active_action = ''

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
    $ _window_hide()
    $ renpy.call_screen(current_room + "Screen")

    return

label Door:
    $ renpy.show_screen(current_room + "Screen")

    e "You move to leave the room, but there's a large stone in the way."

    menu:
        "Turn the doorknob":
            jump NoDoorKnob
        "Politely knock":
            jump KnockOnStone
        "Wink at the rock":
            jump WinkAtRock

label NoDoorKnob:
    e "...Uh."

    e "Nope. No doorknob here."

    e "Just a big rock."

    $ inside_option = False

    jump MyRoom

label KnockOnStone:
    e "You politely knock twice."

    e "..."

    e "No answer."

    e "Probably because it's not a door. It's a rock."

    $ inside_option = False

    jump MyRoom

label WinkAtRock:
    e "You wink at the rock."

    e "..."

    e "Nothing happens."

    e "Which... what did you think would happen?"

    $ inside_option = False

    jump MyRoom

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

label Nail:
    $ renpy.show_screen(current_room + "Screen")

    e "You see a nail sticking out of the wall."

    menu:
        "Hang the mirror on the wall" if 'mirror' in inventory:
            jump HangMirror
        "Take the nail from the wall":
            jump CantTakeNail
        "Leave the nail where it is":
            jump LeaveNail

    $ inside_option = False

    jump MyRoom

label BustedWall:
    $ renpy.show_screen(current_room + "Screen")

    e "Oh, wow! Must have been a false wall!"

    e "Those panels just flew right off!"

    $ inside_option = False

    jump MyRoom

label Scroll:
    $ renpy.show_screen(current_room + "Screen")

    e "Pasted inside the panel you broken open..."

    e "Is a... scroll with writing on it?"

    menu:
        "Read the scroll?":
            jump ReadScroll
        "Don't read the scroll?":
            jump DontReadScroll

label ReadScroll:
    e "You lean up close to the wall to read it..."

    e "{i}Rood nepo{i}..."

    $ scroll_read = True

    jump OpenDoor

label OpenDoor:
    play sound stone_slide

    e "Wow! The Rock Door slides open!"

    e "You escape the room!"

    return

label HangMirror:
    $ mirror_placed = True

    $ inventory.remove('mirror')

    e "Hey, not bad! The mirror really opens up the room!"

    e "Oh, also, it looks like that X in the center of the mirror is pointing to the opposite wall."

    $ inside_option = False

    jump MyRoom

label HangingMirror:
    $ renpy.show_screen(current_room + "Screen")

    e "Hey! It looks like that X in the center of the mirror is pointing to the opposite wall."

    $ inside_option = False

    jump MyRoom

label SecretSpot:
    $ renpy.show_screen(current_room + "Screen")

    if not mirror_placed:
        e "Your eye catches a spot in the wall. You're not sure why..."
    else:
        e "This is about where the mirror's X marks the spot."

    menu:
        "Hit the spot with the Hammer" if 'hammer' in inventory:
                jump HitSpot
        "Scratch at the spot":
                jump ScratchSpot
        "Leave the spot alone":
                jump LeaveSpot

label CantTakeNail:
    e "You pry and pry with all your might..."

    e "..."

    e "Nope, that nail is really stuck in that wall."

    $ inside_option = False

    jump MyRoom

label HitSpot:
    e "You reel back your mighty hammer..."

    play sound rock_smash
    with Shake((0, 0, 0, 0), 0.5, dist=5)

    $ wall_smashed = True

    e "Wham! The wall caves in! And a secret panel opens!"

    $ inside_option = False

    jump MyRoom

label ScratchSpot:
    e "You scratch at the spot."

    e "..."

    e "Nothing happens."

    $ inside_option = False

    jump MyRoom

label LeaveSpot:
    e "You leave the spot alone."

    $ inside_option = False

    jump MyRoom

label LeaveNail:
    e "You leave the nail where it is."

    $ inside_option = False

    jump MyRoom

label TakeMirror:
    $ inventory.append('mirror')

    e "The mirror is now in your inventory!"

    $ inside_option = False

    jump MyRoom

label LeaveMirror:
    e "You leave the mirror where it is."

    $ inside_option = False

    jump MyRoom

label TakeHammer:
    $ inventory.append('hammer')

    e "The hammer is now in your inventory!"

    $ inside_option = False

    jump MyRoom

label LeaveHammer:
    e "You leave the hammer where it is."

    $ inside_option = False

    jump MyRoom

label EnterPuzzleRoom:
    e "You wake up in a mysterious room."

    e "You don't remember how you arrived here. But..."

    e "Or, perhaps, for that reason."

    e "You decide you'd like to leave."

    return
