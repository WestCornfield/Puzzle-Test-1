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

screen LivingRoomScreen():
    add "rooms/Living_Room.png"
    text "Living Room":
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
    textbutton "Go to Living Room":
        at option_one_text_button
        action [SensitiveIf(in_room), SetVariable("current_room", "LivingRoom"), Jump("MyRoom")]
    textbutton "Look at Dinner":
        at option_two_text_button
        action [SensitiveIf(in_room), Jump("LookAtDinner")]
