screen top_tbar():
    frame:
        background None
        xsize 1920
        ysize 75
        
        hbox:  
            xalign 0.0
            text "[DateTime]"
        hbox:
            xalign 0.5
            text Location


        # textbutton _("$" + str(MC.cash)) xalign 0.9 action SetVariable("clickType", "cheat"), Return(100)
        # hbox:
        #     xalign 0.9
        #     button:
        #         text "$" + str(MC.cash)
        #         # text "hello"
        #         action SetVariable("clickType", "cheat"), Return(100)

        hbox:
            xalign 0.9
            text "$" + str(MC.cash)

        # button: 
        #     xalign 0.7
        #     text "$" + str(MC.cash)
        #     action SetVariable("clickType", "cheat"), Return(100)
