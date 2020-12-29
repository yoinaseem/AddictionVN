screen map_icon():
    # zorder 100
    frame:
        background None
        xalign 1.0
        yalign 0.0
        imagebutton:
            idle "ui/map/mapicon.png"
            hover "ui/map/mapiconhovered.png" 
            action ToggleVariable("navMenu")
            hovered tt.Action("Toggle Map")
