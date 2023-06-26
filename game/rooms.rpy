transform room_text:
    xpos 50
    ypos 100

transform move_count_text:
    xpos 50
    ypos 200

transform option_one_text_button:
    xpos 50
    ypos 300

transform option_two_text_button:
    xpos 50
    ypos 400

transform resting_on_table:
    xpos 800
    ypos 350

image hammer_idle:
    "objects/hammer/idle/frame_01.png"
    pause 2.0
    "objects/hammer/idle/frame_02.png"
    pause 0.1
    "objects/hammer/idle/frame_03.png"
    pause 0.1
    "objects/hammer/idle/frame_04.png"
    pause 0.1
    "objects/hammer/idle/frame_05.png"
    pause 0.1
    "objects/hammer/idle/frame_06.png"
    pause 0.1
    "objects/hammer/idle/frame_07.png"
    pause 0.1
    "objects/hammer/idle/frame_08.png"
    pause 0.1
    "objects/hammer/idle/frame_09.png"
    pause 0.1
    "objects/hammer/idle/frame_10.png"
    pause 0.1
    "objects/hammer/idle/frame_11.png"
    pause 0.1
    "objects/hammer/idle/frame_12.png"
    pause 0.1
    repeat

screen PuzzleRoomScreen():
    add "rooms/Puzzle_Room.png"
    if not 'hammer' in inventory:
        imagebutton:
            idle "hammer_idle"
            at resting_on_table
            action [SensitiveIf(in_room), Jump("Hammer")]
    text "Puzzle Room":
        at room_text
    text "Move Count: " + str(move_count):
        at move_count_text
    textbutton "Go to Dining Room":
        at option_one_text_button
        action [SensitiveIf(in_room), SetVariable("current_room", "DiningRoom"), Jump("MyRoom")]
    textbutton "End Game":
        at option_two_text_button
        action [SensitiveIf(in_room), Jump("EndGame")]

screen DiningRoomScreen():
    text "Dining Room":
        at room_text
    text "Move Count: " + str(move_count):
        at move_count_text
    textbutton "Go to Puzzle Room":
        at option_one_text_button
        action [SensitiveIf(in_room), SetVariable("current_room", "PuzzleRoom"), Jump("MyRoom")]
    textbutton "Look at Dinner":
        at option_two_text_button
        action [SensitiveIf(in_room), Jump("LookAtDinner")]
