screen Main_UI():
    use BGIMAGE
    use top_tbar
    use ClickyScreen
    if navMenu:
        use NavMap
    if Notification:
        add "ui/Notif.png"

    use TipScreen

    # frame:
    #     background None 
    #     hbox:
    #         xalign 1.0
    #         yalign 0.0
    #     # textbutton _("Open Map") action (Hide("map_screen"), Show("MapScreen")), Return(0)
    #         imagebutton:
    #             idle "mapicon"
    #             hover "mapiconhovered" 
    #             action Call("OpenMap"), Hide("map_screen")   