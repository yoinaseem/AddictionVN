screen map_icon():    
    imagebutton:
        xalign 1.0
        idle "ui/map/mapicon.png"
        hover "ui/map/mapiconhovered.png" 
        action ToggleVariable("navMenu")
        # hovered tt.Action("Toggle Map")
    
    if clickType == "Character" or clickType == "Object":
        imagebutton:
            xalign 1.0
            idle "ui/map/mapicon.png"
            hover "ui/map/mapicon.png" 
            action NullAction()