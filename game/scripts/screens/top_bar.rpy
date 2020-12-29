screen top_tbar():
    # frame:
    #     xpos 0
    #     ypos 0
    #     xsize 1920
    #     ysize 75
    hbox:  
        xalign 0.0
        text "[DateTime]"
    hbox:
        xalign 0.5
        text Location

    button:
        xalign 0.9
        text "$" + str(MC.cash)
        action SetVariable("clickType", "cheat"), Return(100)
