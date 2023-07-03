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
define nail_removed = False
define scroll_read = False
define broke_mirror = False

define open_menu = False
define open_inventory = False
define active_action = ''
define selected_item = ''
define option_text = ''
define player_statement = ''

define timesScrollUnread = 0

define gameOver = False

# The game starts here.

label start:
    e "Here is the start of your game."

    #Call the first scene
    $ current_room = "PuzzleRoom"
    call MyRoom from _call_MyRoom

    e "You finished the game!"

    return

label MyRoom:
    if gameOver == True:
        return

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

label goodEnding:
    $ gameOver = True
    return

label handleObjectClick:
    $ renpy.show_screen(current_room + "Screen")
    $ open_menu = False
    $ inside_option = True
    return

label handleObjectClickWrapUp:
    $ active_action = ''
    $ selected_item = ''
    $ option_text = ''
    return

label handleTalkClick:
    $ renpy.show_screen(current_room + "Screen")
    $ active_action = 'talk'
    $ selected_item = ''
    $ option_text = 'Talk to what?'
    jump MyRoom

label handleTakeClick:
    $ renpy.show_screen(current_room + "Screen")
    $ active_action = 'take'
    $ selected_item = ''
    $ option_text = 'Take what?'
    jump MyRoom

label handleLookClick:
    $ renpy.show_screen(current_room + "Screen")
    $ active_action = 'look'
    $ selected_item = ''
    $ option_text = 'Look at what?'
    jump MyRoom

label handleMirrorClick:
    $ renpy.show_screen(current_room + "Screen")
    $ active_action = ''
    $ selected_item = 'mirror'
    $ option_text = 'Use Mirror with what?'
    jump MyRoom

label handleHammerClick:
    $ renpy.show_screen(current_room + "Screen")
    $ active_action = ''
    $ selected_item = 'hammer'
    $ option_text = 'Use Hammer with what?'
    jump MyRoom

label handleInventoryObjectClick(object=''):
    $ renpy.show_screen(current_room + "Screen")
    $ active_action = ''
    $ selected_item = object
    $ option_text = 'Use {} on what?'.format(object)
    jump MyRoom

label Door:
    call handleObjectClick from _call_handleObjectClick

    if active_action == 'take' or active_action == '':
        e "You move to leave the room, but there's a large stone in the way."

        menu:
            "Turn the doorknob":
                call NoDoorKnob from _call_NoDoorKnob
            "Politely knock":
                call KnockOnStone from _call_KnockOnStone
            "Wink at the rock":
                call WinkAtRock from _call_WinkAtRock
            "Speak to the door":
                call SpeakToDoor

    elif active_action == 'look':
        e "On the other side of the room, is a large stone slab where a door usually would go."
        e "Hmm, There's no handle or clear way to open the rock."

    elif active_action == 'talk':
        call SpeakToDoor

    $ inside_option = False

    call handleObjectClickWrapUp from _call_handleObjectClickWrapUp

    jump MyRoom

label SpeakToDoor:
    e "You clear your throat."
    $ player_statement = renpy.input("What do you say to the door?", length=32).lower()

    if not player_statement:
        e "You suddenly become shy and your tongue sticks in your throat!"
        e "Don't be nervous! I'm sure you and this giant rock have many common interests!"
    elif player_statement == 'hello':
        e "'Hello!' you say, putting your friendliest foot forward!"
        e "..."
        e "Rudely, the stone ignores you."
    elif player_statement == 'open':
        e "'Open!' you say commandingly, authoritatively! Like it would be in the rock's best interest to do as you say!"
        e "..."
        e "Defiantly, the rock remains in place."
    elif player_statement == 'open please' or player_statement == 'please open':
        e "'Open please!' you say politely, but firmly!"
        e "..."
        e "What?!? The rock remains in place?!?"
        e "...But. You said please!"
    elif player_statement == 'open sesame':
        e "'Open sesame!' you call out!"
        e "..."
        e "The rock doesn't move!"
        e "Oh, come ON! That always works!"
    elif player_statement == 'rood nepo':
        e "'Rood nepo!' you call out!"
        jump OpenDoor
    else:
        e "You speak passionately and from the heart!"
        e "'[player_statement]!'"
        e "..."
        e "The rock is unmoved."
        e "Literally."
        e "Womp womp."

    return

label NoDoorKnob:
    e "...Uh."
    e "Nope. No doorknob here."
    e "Just a big rock."

    return

label KnockOnStone:
    e "You politely knock twice."
    e "..."
    e "No answer."
    e "Probably because it's not a door. It's a rock."

    return

label WinkAtRock:
    e "You wink at the rock."
    e "..."
    e "Nothing happens."
    e "Perhaps the rock is shy and you were too forward?"

    return

label Hammer:
    call handleObjectClick from _call_handleObjectClick_1

    if active_action == 'take' or active_action == '':
        call TakeHammer from _call_TakeHammer

    elif active_action == 'look':
        e "On the table in the puzzle room, there's a hammer."
        e "It's shimmering. Even the wooden handle, which is odd."

    elif active_action == 'talk':
        e "'Salutations!' you say, extending your hand!"
        e "..."
        e "Rudely, the hammer refuses to shake your hand."

    $ inside_option = False

    call handleObjectClickWrapUp from _call_handleObjectClickWrapUp_1

    jump MyRoom

label Mirror:
    call handleObjectClick from _call_handleObjectClick_2

    if selected_item == 'hammer':
        e "...Okay. Just checking."
        e "I understand the potential confusion."
        e "There's an X drawn on it."
        e "Maybe, you're thinking like... The X means strike here!"
        e "And I will tell you, the game is still winnable without the mirror."
        e "The solution is just... MUCH LESS obvious."
        e "So. Are you *sure* you want to smash the mirror?"
        menu:
            "Yes":
                jump SmashMirror
            "No":
                e "Phew, okay."
                e "I mean, I don't want to limit your freedom of choice."
                e "But, I think that's a good move."
    elif active_action == 'take' or active_action == '':
        call TakeMirror from _call_TakeMirror
    elif active_action == 'look':
        e "Against the wall of the puzzle room, there's a mirror."
        e "It looks like it has a black X on its center... What could that mean?"
    elif active_action == 'talk':
        e "'Greetings!' you say, waving politely!"
        e "...Hey!"
        e "The mirror is waving back!"
        e "Finally, something in this room has manners!"

    $ inside_option = False

    call handleObjectClickWrapUp from _call_handleObjectClickWrapUp_2

    jump MyRoom

label BrokenMirror:
    call handleObjectClick

    if selected_item == 'hammer':
        e "...The mirror is already very smashed."
        e "And you make a mental note that some emotional counseling might help with your desire to randomly desire property."
    elif active_action == 'take' or active_action == '':
        call TakeMirror
    elif active_action == 'look':
        e "Against the wall of the puzzle room, there's a mirror."
        e "Y'know. The one you smashed with a hammer."
        e "That's seven years of bad luck!"
    elif active_action == 'talk':
        e "'Greetings!' you say, waving politely!"
        e "..."
        e "You can't make out your reflection any more."

    $ inside_option = False

    call handleObjectClickWrapUp

    jump MyRoom

label SmashMirror:
    $ broke_mirror = True

    e "KERASH!"
    e "The mirror shatters!"
    e "..."
    e "Okay, I'm respecting your choice."
    e "Good luck from here."

    $ inside_option = False

    call handleObjectClickWrapUp

    jump MyRoom

label Nail:
    call handleObjectClick from _call_handleObjectClick_3

    if selected_item == 'mirror' or selected_item == 'broken_mirror':
        call HangMirror from _call_HangMirror
    elif selected_item == 'hammer':
        call TakeNail
    elif active_action == 'take' or active_action == '':
        call CantTakeNail from _call_CantTakeNail
    elif active_action == 'look':
        e "You see a nail sticking out of the wall."
    elif active_action == 'talk':
        e "'Hiya!' you say, smiling politely."
        e "..."
        e "The nail says nothing, looking down on you from its perch on the wall."

    $ inside_option = False

    call handleObjectClickWrapUp from _call_handleObjectClickWrapUp_3

    jump MyRoom

label NailHole:
    call handleObjectClick

    if selected_item == 'mirror':
        e "Hmm... You try to put the mirror on the wall."
        e "Unfortunately, there's nothing for it to rest on..."
        e "Didn't something used to be at this spot?"
    elif selected_item == 'hammer':
        e "You already pulled the nail out."
        e "And there's probably a way out of the room without taking out a potentially load-bearing wall."
        e "..."
        e "Probably."
    elif selected_item == 'nail':
        $ nail_removed = False
        $ inventory.remove('nail')
        e "The nail slips back into the hole securely."
    elif active_action == 'take' or active_action == '':
        e "You want to take a hole?"
        e "A hole is the absence of space!"
        e "You can't take what ISN'T!"
    elif active_action == 'look':
        e "The hole in the wall where the nail used to be."
    elif active_action == 'talk':
        e "'Hiya!' you say, smiling politely."
        e "..."
        e "The hole says nothing, snootily."

    $ inside_option = False

    call handleObjectClickWrapUp

    jump MyRoom

label BustedWall:
    call handleObjectClick from _call_handleObjectClick_4

    e "Oh, wow! Must have been a false wall!"
    e "Those panels just flew right off!"

    $ inside_option = False

    call handleObjectClickWrapUp from _call_handleObjectClickWrapUp_4

    jump MyRoom

label Scroll:
    call handleObjectClick from _call_handleObjectClick_5

    e "Pasted inside the panel you broken open..."
    e "Is a... scroll with writing on it?"

    menu:
        "Read the scroll?":
            jump ReadScroll
        "Don't read the scroll?":
            jump DontReadScroll

label ReadScroll:
    e "You lean up close to the wall to read it..."
    e "{i}Rood nepo{i}...?"
    e "...What does that mean?"

    $ inside_option = False

    call handleObjectClickWrapUp

    jump MyRoom

label DontReadScroll:
    e "You decide not to read the scroll."
    e "..."
    e "Which is fair."
    e "I mean, there's so much more to do in this room, right?"

    $ inside_option = False

    call handleObjectClickWrapUp

    jump MyRoom

label OpenDoor:
    call handleObjectClick from _call_handleObjectClick_6

    $ scroll_read = True

    play sound stone_slide

    e "Wow! The Rock Door slides open!"
    e "You escape the room!"

    call handleObjectClickWrapUp from _call_handleObjectClickWrapUp_5

    jump goodEnding

label HangMirror:
    $ mirror_placed = True

    if not broke_mirror:
        $ inventory.remove('mirror')

        e "Hey, not bad! The mirror really opens up the room!"
        e "Oh, also, it looks like that X in the center of the mirror is pointing to the opposite wall."
    else:
        $ inventory.remove('broken_mirror')
        e "I mean, that's an interior design choice."
        e "What is a mirror but a reflection? A projection? A distortion!"
        e "And a broken mirror is a demand to deny yourself these distortions!"
        e "To face reality!"
        e "What a statement! Brava! Bold! Daring!"

    return

label HangingMirror:
    call handleObjectClick from _call_handleObjectClick_7

    if not broke_mirror:
        if active_action == 'take' or active_action == '':
            $ inventory.append('mirror')
            $ mirror_placed = False
            e "You take the mirror off the wall."
            e "You room feels smaller, but that's just feng shui. It's still the same size, actually."
        elif active_action == 'look':
            e "Hey! It looks like that X in the center of the mirror is pointing to the opposite wall."
        elif active_action == 'talk':
            e "'Hi!' You wave at the mirror you've hung on the wall!"
            e "Your reflection waves back!"
    else:
        if active_action == 'take' or active_action == '':
            $ inventory.append('broken_mirror')
            $ mirror_placed = False
            e "You take the broken mirror off the wall, careful not to cut yourself on the shards of glass."
        elif active_action == 'look':
            e "Hmm, it's hard to make out what the mirror might have indicated..."
            e "Although you do remember an X in its center."
        elif active_action == 'talk':
            e "'Hi!' You wave at the broken mirror you've hung on the wall!"
            e "..."
            e "Nothing happens, though."

    $ inside_option = False

    call handleObjectClickWrapUp from _call_handleObjectClickWrapUp_6

    jump MyRoom

label SecretSpot:
    call handleObjectClick from _call_handleObjectClick_8

    if selected_item == 'hammer':
        call HitSpot from _call_HitSpot
    elif active_action == 'look':
        if not mirror_placed:
            e "Your eye catches a spot in the wall. You're not sure why..."
        else:
            e "This is about where the mirror's X marks the spot."
    elif active_action == 'take' or active_action == '':
        call ScratchSpot from _call_ScratchSpot
    elif active_action == 'talk':
        e "'Howdy!' you say to a specific spot on the wall!"
        e "..."
        e "The wall remains silent."

    $ inside_option = False

    call handleObjectClickWrapUp from _call_handleObjectClickWrapUp_7

    jump MyRoom

label TakeNail:
    e "You turn the hammer around, set the back of its head against the nail and..."

    $ nail_removed = True

    $ inventory.append('nail')

    e "Pop! The nail comes out! There, now, there's not a nail sticking out of the wall."

    e "The nail is now in your inventory!"

    e "...Still."

    e "That leaves an unsightly hole in the wall."

    e "Maybe, you can find a bit of caulk somewhere, you can plug up the hole."

    e "Then, you just need some tasteful art, maybe found at a local market, so the wall looks less empty."

    e "Ooh, or maybe a fake bowl of fruit for color?"

    e "..."

    e "...Wait."

    e "What are you trying to do again?"

    e "..."

    e "Oh! That's right! Escape!"

    return

label CantTakeNail:
    e "You pry and pry with all your might..."

    e "..."

    e "Nope, that nail is really stuck in that wall."

    return

label HitSpot:
    e "You reel back your mighty hammer..."

    play sound rock_smash
    with Shake((0, 0, 0, 0), 0.5, dist=5)

    $ wall_smashed = True

    e "Wham! The wall caves in! And a secret panel opens!"

    return

label ScratchSpot:
    e "You scratch at the spot."
    e "..."
    e "Nothing happens."

    return

label TakeMirror:
    if not broke_mirror:
        $ inventory.append('mirror')
        e "The mirror is now in your inventory!"
    else:
        $ inventory.append('broken_mirror')
        e "The broken mirror is now in your inventory!"

    return

label TakeHammer:
    $ inventory.append('hammer')
    e "The hammer is now in your inventory!"

    return

label EnterPuzzleRoom:
    e "You wake up in a mysterious room."
    e "You don't remember how you arrived here. But..."
    e "Or, perhaps, *because* you can't remember..."
    e "You decide you'd like to leave."

    return
