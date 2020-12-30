screen NavMap():
    frame:
        background None
        xalign 0.0
        yalign 0.0
        xsize 1920
        ysize 1080
        add "ui/map/map_bg.jpg"

        button:
            xpos 0
            ypos 0
            text "Return"
            action Return(Location)
     
        for q in Places:
            if q.isActive:
                imagebutton: 
                    xpos q.x
                    ypos q.y
                    hover q.MapIcon
                    idle q.MapIcon
                    focus_mask True
                    action SetVariable("clickType", "Nav"), ToggleVariable("navMenu"), Return(q.name)
                    hovered tt.Action("Go to " + q.name)
