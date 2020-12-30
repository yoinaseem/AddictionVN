label NoLabel:
    $ Notification = True
    "I can't do that right now..."

label bong_Clicked:
    $ Notification = True
    menu:
        "Hit the bong":
            "Goddamn..."
            "...that got me pretty high."
            $ calendar.AdvanceTime(1)
            $ isHigh = True
        "Back":
            return
return

label bed_Clicked:
    $ Notification = True    
    menu: 
        "Go to Sleep":
            $ calendar.AdvanceTime(8)
            $ isHigh = False 
        "Back":
            return

return

