screen LivingRoomScreen():
    vbox:
        text "Living Room"
        text "Move Count: " + str(move_count)
        textbutton "Go to Dining Room":
            action [SensitiveIf(in_room), SetVariable("current_room", "DiningRoom"), Jump("MyRoom")]
        textbutton "End Game":
            action [SensitiveIf(in_room), Jump("EndGame")]

screen DiningRoomScreen():
    vbox:
        text "Dining Room"
        text "Move Count: " + str(move_count)
        textbutton "Go to Living Room":
            action [SensitiveIf(in_room), SetVariable("current_room", "LivingRoom"), Jump("MyRoom")]
        textbutton "Look at Dinner":
            action [SensitiveIf(in_room), Jump("LookAtDinner")]
