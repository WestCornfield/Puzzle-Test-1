transform resting_on_table:
    xpos 850
    ypos 350

transform resting_on_wall:
    xpos 300
    ypos 280

transform nail_in_wall:
    xpos 80
    ypos 200

transform mirror_on_wall:
    xpos 50
    ypos 150

transform secret_spot:
    xpos 1136
    ypos 344

transform hidden_panel:
    xpos 1088
    ypos 204

transform scroll_location:
    xpos 1132
    ypos 316

transform door_location:
    xpos 464
    ypos 176

transform dropdown_button_location:
    ypos 0
    xpos 568

transform open_dropdown_button_location:
    ypos 0
    xpos 568
    ease 1 xpos 568 ypos 128
    ease 1 xpos 568 ypos 112

transform open_user_interface_location:
    ypos -130
    xpos 0
    ease 1 xpos 0 ypos 0
    ease 1 xpos 0 ypos -16

transform open_look_button_location:
    ypos -110
    xpos 28
    ease 1 xpos 28 ypos 32
    ease 1 xpos 28 ypos 16

transform open_talk_button_location:
    ypos -110
    xpos 132
    ease 1 xpos 132 ypos 28
    ease 1 xpos 132 ypos 12

transform open_take_button_location:
    ypos -110
    xpos 248
    ease 1 xpos 248 ypos 28
    ease 1 xpos 248 ypos 12

transform open_inventory_button_location:
    ypos -110
    xpos 352
    ease 1 xpos 352 ypos 28
    ease 1 xpos 352 ypos 12

transform root_inventory_menu_location:
    ypos 100
    xpos 100

transform up_arrow_inventory_location:
    ypos 125
    xpos 1000

transform down_arrow_inventory_location:
    ypos 275
    xpos 1000

transform look_inventory_location:
    ypos 380
    xpos 130

transform use_inventory_location:
    ypos 380
    xpos 270

transform close_inventory_location:
    ypos 380
    xpos 710

transform inventory_spot(spot_number):
    ypos 140
    xpos (150 + (spot_number * 100))

#user interface idle assets
image dropdown_button_idle = "user_interface/dropdown/button/idle/Dropdown_Button.png"
image dropdown_button_inversed_idle = "user_interface/dropdown/button/idle/Dropdown_Button_inversed_resized.png"
image user_interface_idle = "user_interface/dropdown/interaction_panel/interaction_panel_resized.png"

image look_button_idle = "user_interface/icons/look/idle/eyeball.png"
image talk_button_idle = "user_interface/icons/talk/idle/talk.png"
image take_button_idle = "user_interface/icons/take/idle/take.png"
image inventory_button_idle = "user_interface/icons/inventory/idle/inventory.png"

#inventory interface idle assets
image root_inventory_idle = "user_interface/inventory/background/root/idle/root_inventory_menu.png"
image up_arrow_inventory_idle = "user_interface/inventory/background/icons/up_arrow/idle.png"
image down_arrow_inventory_idle = "user_interface/inventory/background/icons/down_arrow/idle.png"
image look_inventory_idle = "user_interface/inventory/background/icons/look/idle.png"
image use_inventory_idle = "user_interface/inventory/background/icons/use/idle.png"
image close_inventory_idle = "user_interface/inventory/background/icons/close/idle.png"

image hammer_inventory_icon = "user_interface/inventory/icons/hammer/idle/hammer.png"
image mirror_inventory_icon = "user_interface/inventory/icons/mirror/idle/mirror.png"

#user interface hover assets
image look_button_hover:
    "user_interface/icons/look/hover/frame_00.png"
    pause 0.5
    "user_interface/icons/look/hover/frame_01.png"
    pause 0.1
    "user_interface/icons/look/hover/frame_02.png"
    pause 0.3
    "user_interface/icons/look/hover/frame_01.png"
    pause 0.1
    "user_interface/icons/look/hover/frame_00.png"
    pause 0.1
    "user_interface/icons/look/hover/frame_03.png"
    pause 0.1
    "user_interface/icons/look/hover/frame_04.png"
    pause 0.3
    "user_interface/icons/look/hover/frame_03.png"
    pause 0.1
    repeat

image talk_button_hover:
    "user_interface/icons/talk/hover/frame_00.png"
    pause 0.5
    "user_interface/icons/talk/hover/frame_01.png"
    pause 0.1
    "user_interface/icons/talk/hover/frame_02.png"
    pause 0.1
    "user_interface/icons/talk/hover/frame_03.png"
    pause 0.1
    repeat

image take_button_hover:
    "user_interface/icons/take/hover/frame_00.png"
    pause 0.5
    "user_interface/icons/take/hover/frame_01.png"
    pause 0.1
    "user_interface/icons/take/hover/frame_02.png"
    pause 0.1
    "user_interface/icons/take/hover/frame_03.png"
    pause 0.5
    "user_interface/icons/take/hover/frame_02.png"
    pause 0.1
    "user_interface/icons/take/hover/frame_01.png"
    pause 0.1
    repeat

image inventory_button_hover:
    "user_interface/icons/inventory/hover/frame_00.png"
    pause 1
    "user_interface/icons/inventory/hover/frame_01.png"
    pause 0.1
    "user_interface/icons/inventory/hover/frame_02.png"
    pause 0.3
    "user_interface/icons/inventory/hover/frame_03.png"
    pause 0.1
    "user_interface/icons/inventory/hover/frame_04.png"
    pause 0.1
    "user_interface/icons/inventory/hover/frame_02.png"
    pause 1
    "user_interface/icons/inventory/hover/frame_01.png"
    pause 0.1
    repeat

#in-game idle assets
image hanging_mirror_idle = "objects/mirror/hanged/idle/Hanged_Mirror.png"
image mirror_idle = "objects/mirror/idle/Mirror.png"
image hammer_idle = "objects/hammer/idle/Hammer.png"
image nail_idle = "objects/nail/idle/Nail.png"
image busted_wall_idle = "objects/busted_wall/idle_with_scroll.png"
image scroll_idle = "objects/scroll/idle/scroll.png"
image secret_spot_idle = "objects/secret_spot/idle/Spot.png"
image rock_door_closed_idle = "objects/doors/rock_door/idle/closed/rock_door.png"
image rock_door_open_idle = "objects/doors/rock_door/idle/open/rock_door.png"

image rock_door_opening:
    "objects/doors/rock_door/animation/opening_animation/frame_01.png"
    pause 0.5
    "objects/doors/rock_door/animation/opening_animation/frame_02.png"
    pause 0.1
    "objects/doors/rock_door/animation/opening_animation/frame_03.png"
    pause 0.1
    "objects/doors/rock_door/animation/opening_animation/frame_04.png"
    pause 0.1
    "objects/doors/rock_door/animation/opening_animation/frame_05.png"
    pause 0.1
    "objects/doors/rock_door/animation/opening_animation/frame_06.png"
    pause 0.1
    "objects/doors/rock_door/animation/opening_animation/frame_07.png"
    pause 0.1
    "objects/doors/rock_door/animation/opening_animation/frame_08.png"
    pause 0.1
    "objects/doors/rock_door/animation/opening_animation/frame_09.png"
    pause 0.1
    "objects/doors/rock_door/animation/opening_animation/frame_10.png"
    pause 0.1
    "objects/doors/rock_door/animation/opening_animation/frame_11.png"
    pause 0.1
    "objects/doors/rock_door/animation/opening_animation/frame_12.png"
    pause 0.1
    "objects/doors/rock_door/animation/opening_animation/frame_13.png"
    pause 0.1
    "objects/doors/rock_door/animation/opening_animation/frame_14.png"
    pause 0.1

image hanging_mirror_hover:
    "objects/mirror/hanged/hover/frame_00.png"
    pause 2.0
    "objects/mirror/hanged/hover/frame_01.png"
    pause 0.1
    "objects/mirror/hanged/hover/frame_02.png"
    pause 0.1
    "objects/mirror/hanged/hover/frame_03.png"
    pause 0.1
    "objects/mirror/hanged/hover/frame_04.png"
    pause 0.1
    "objects/mirror/hanged/hover/frame_05.png"
    pause 0.1
    "objects/mirror/hanged/hover/frame_06.png"
    pause 0.1
    "objects/mirror/hanged/hover/frame_07.png"
    pause 0.1
    repeat

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
    add "rooms/PuzzleRoom/Puzzle_Room_Basic.png"
    if not open_menu and not open_inventory:
        imagebutton:
            idle "dropdown_button_idle"
            at dropdown_button_location
            action [SensitiveIf(not inside_option), SetVariable("open_menu", True)]
    if open_menu and not open_inventory:
        imagebutton:
            idle "dropdown_button_inversed_idle"
            at open_dropdown_button_location
            action [SensitiveIf(not inside_option), SetVariable("open_menu", False)]
        imagebutton:
            idle "user_interface_idle"
            at open_user_interface_location
        imagebutton:
            auto "look_button_%s"
            at open_look_button_location
            action [SensitiveIf(not inside_option), SetVariable("active_action", 'look')]
        imagebutton:
            auto "talk_button_%s"
            at open_talk_button_location
            action [SensitiveIf(not inside_option), SetVariable("active_action", 'talk')]
        imagebutton:
            auto "take_button_%s"
            at open_take_button_location
            action [SensitiveIf(not inside_option), SetVariable("active_action", 'take')]
        imagebutton:
            auto "inventory_button_%s"
            at open_inventory_button_location
            action [SensitiveIf(not inside_option), SetVariable("open_menu", False), SetVariable("open_inventory", True)]
    if wall_smashed:
        imagebutton:
            idle "busted_wall_idle"
            at hidden_panel
            action [SensitiveIf(in_room and not inside_option), SetVariable("open_menu", False), SetVariable("inside_option", True), Jump("BustedWall")]
    if wall_smashed and not 'scroll' in inventory:
        imagebutton:
            idle "scroll_idle"
            at scroll_location
            action [SensitiveIf(in_room and not inside_option), SetVariable("open_menu", False), SetVariable("inside_option", True), Jump("Scroll")]
    if not scroll_read:
        imagebutton:
            idle "rock_door_closed_idle"
            at door_location
            action [SensitiveIf(in_room and not inside_option), SetVariable("open_menu", False), SetVariable("inside_option", True), Jump("Door")]
    if scroll_read:
        imagebutton:
            idle "rock_door_opening"
            at door_location
    if not mirror_placed and not 'mirror' in inventory:
        imagebutton:
            auto "mirror_%s"
            at resting_on_wall
            action [SensitiveIf(in_room and not inside_option), SetVariable("open_menu", False), SetVariable("open_menu", False), SetVariable("inside_option", True), Jump("Mirror")]
    if not 'hammer' in inventory:
        imagebutton:
            auto "hammer_%s"
            at resting_on_table
            action [SensitiveIf(in_room and not inside_option), SetVariable("open_menu", False), SetVariable("inside_option", True), Jump("Hammer")]
    if not mirror_placed:
        imagebutton:
            auto "nail_%s"
            at nail_in_wall
            action [SensitiveIf(in_room and not inside_option), SetVariable("open_menu", False), SetVariable("inside_option", True), Jump("Nail")]
    if mirror_placed:
        imagebutton:
            auto "hanging_mirror_%s"
            at mirror_on_wall
            action [SensitiveIf(in_room and not inside_option), SetVariable("open_menu", False), SetVariable("inside_option", True), Jump("HangingMirror")]
    if not wall_smashed:
        imagebutton:
            idle "secret_spot_idle"
            at secret_spot
            action [SensitiveIf(in_room and not inside_option), SetVariable("open_menu", False), SetVariable("inside_option", True), Jump("SecretSpot")]
    if open_inventory:
        imagebutton:
            idle "root_inventory_idle"
            at root_inventory_menu_location
        imagebutton:
            idle "up_arrow_inventory_idle"
            at up_arrow_inventory_location
        imagebutton:
            idle "down_arrow_inventory_idle"
            at down_arrow_inventory_location
        imagebutton:
            idle "look_inventory_idle"
            at look_inventory_location
        imagebutton:
            idle "use_inventory_idle"
            at use_inventory_location
        imagebutton:
            idle "close_inventory_idle"
            at close_inventory_location
            action [SensitiveIf(in_room and not inside_option), SetVariable("open_inventory", False)]
        for item in inventory:
            imagebutton:
                idle "{}_inventory_icon".format(item)
                at inventory_spot(inventory.index(item))
                action [SensitiveIf(in_room and not inside_option), SetVariable("selected_item", item)]
