screen calendar_screen():
      hbox:
         text "[Output]"
         # text calendar.Output()

screen MapScreen():
    frame:
        xalign 0.0
        yalign 0.0
        xsize 1920
        ysize 1080
        background "map.jpg"
        
        for q in Places:
            if q.isActive:
                button: 
                    xpos q.x
                    ypos q.y
                    text q.name
                    action Return(q.name)

        # button: 
        #     xpos 700
        #     ypos 300
        #     text "Living Room"
        #     action Return("Dorm")


