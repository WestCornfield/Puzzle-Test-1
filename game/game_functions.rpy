init python:
    def update_gamestate():
        global move_count
        newcount = move_count + 1
        SetVariable("move_count", newcount)()
        return

    def check_intro_reactions(room):
        if room == "PuzzleRoom":
            renpy.call("EnterPuzzleRoom")
        elif room == "DiningRoom":
            renpy.call("EnterDiningRoom")
        return
