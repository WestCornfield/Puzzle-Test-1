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
    xpos 850
    ypos 350

transform resting_on_wall:
    xpos 300
    ypos 280

transform nail_in_wall:
    xpos 80
    ypos 200

image mirror_idle = "objects/mirror/idle/Mirror.png"

image hammer_idle = "objects/hammer/idle/Hammer.png"

image nail_idle = "objects/nail/idle/Nail.png"

image hammer_hover:
    "objects/hammer/hover/frame_01.png"
    pause 2.0
    "objects/hammer/hover/frame_02.png"
    pause 0.1
    "objects/hammer/hover/frame_03.png"
    pause 0.1
    "objects/hammer/hover/frame_04.png"
    pause 0.1
    "objects/hammer/hover/frame_05.png"
    pause 0.1
    "objects/hammer/hover/frame_06.png"
    pause 0.1
    "objects/hammer/hover/frame_07.png"
    pause 0.1
    "objects/hammer/hover/frame_08.png"
    pause 0.1
    "objects/hammer/hover/frame_09.png"
    pause 0.1
    "objects/hammer/hover/frame_10.png"
    pause 0.1
    "objects/hammer/hover/frame_11.png"
    pause 0.1
    "objects/hammer/hover/frame_12.png"
    pause 0.1
    repeat

image mirror_hover:
    "objects/mirror/hover/frame_00.png"
    pause 2.0
    "objects/mirror/hover/frame_01.png"
    pause 0.1
    "objects/mirror/hover/frame_02.png"
    pause 0.1
    "objects/mirror/hover/frame_03.png"
    pause 0.1
    "objects/mirror/hover/frame_04.png"
    pause 0.1
    "objects/mirror/hover/frame_05.png"
    pause 0.1
    "objects/mirror/hover/frame_06.png"
    pause 0.1
    "objects/mirror/hover/frame_07.png"
    pause 0.1
    repeat

image nail_hover:
    "objects/nail/hover/frame_00.png"
    pause 2.0
    "objects/nail/hover/frame_01.png"
    pause 0.1
    "objects/nail/hover/frame_02.png"
    pause 0.1
    "objects/nail/hover/frame_03.png"
    pause 0.1
    "objects/nail/hover/frame_04.png"
    pause 0.1
    repeat

screen PuzzleRoomScreen():
    if mirror_placed:
        add "rooms/PuzzleRoom/Puzzle_Room_No_Mirror.png"
    if not mirror_placed:
        add "rooms/PuzzleRoom/Puzzle_Room_No_Mirror.png"
    if not 'mirror' in inventory:
        imagebutton:
            auto "mirror_%s"
            at resting_on_wall
            action [SensitiveIf(in_room), Jump("Mirror")]
    if not 'hammer' in inventory:
        imagebutton:
            auto "hammer_%s"
            at resting_on_table
            action [SensitiveIf(in_room), Jump("Hammer")]
    if not mirror_placed:
        imagebutton:
            auto "nail_%s"
            at nail_in_wall
            action [SensitiveIf(in_room), Jump("Nail")]
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
