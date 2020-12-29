screen Main_UI():
    frame:
        background None 
        hbox:
            xalign 1.0
            yalign 0.0
        # textbutton _("Open Map") action (Hide("map_screen"), Show("MapScreen")), Return(0)
            imagebutton:
                idle "mapicon"
                hover "mapiconhovered" 
                action Call("OpenMap"), Hide("map_screen")   