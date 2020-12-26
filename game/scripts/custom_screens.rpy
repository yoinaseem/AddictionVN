screen calendar_screen():
      hbox:
         text "[Output]"
         # text calendar.Output()

screen map_screen():
    hbox:
        xalign 1.0
        yalign 0.0
        # textbutton _("Open Map") action (Hide("map_screen"), Show("MapScreen")), Return(0)
        imagebutton:
            idle "mapicon"
            hover "mapiconhovered" 
            action Call("OpenMap"), Hide("map_screen")


screen MapScreen():
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
            if q.isActive:
                button: 
                    xpos q.x
                    ypos q.y
                    text q.name
                    action Return(q.name), #ToggleScreen("MapScreen")

        # button: 
        #     xpos 700
        #     ypos 300
        #     text "Living Room"
        #     action Return("Dorm")


