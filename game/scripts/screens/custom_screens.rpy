screen calendar_screen():
      hbox:
         text "[Output]"

screen map_screen():
    zorder 100
    hbox:
        xalign 1.0
        yalign 0.0
        imagebutton:
            idle "mapicon"
            hover "mapiconhovered" 
            action Call("OpenMap"), Hide("map_screen")


screen MapScreen():
    zorder 100
    modal True
    frame:
        xalign 0.0
        yalign 0.0
        xsize 1920
        ysize 1080
        background "map.jpg"

        button:
            xpos 100
            ypos 100
            textbutton _("Return") action ToggleScreen("MapScreen")
        
        for q in Places:
            if q.unlocked:
                button: 
                    xpos q.x
                    ypos q.y
                    text q.name
                    action Return(q.name)


