label start:

    call variables


    $ GameRunning = True
    while GameRunning:
        window hide
        $ Notification = False 
        $ clickType = ""
        $ UIreturn = renpy.call_screen("Main_UI", _layer="screens")

        if clickType == "Nav":
            $ Location = UIreturn

        if clickType == "Object":
            call expression UIreturn

        if clickType == "cheat":
            $ MC.cash += 100

        $ DateTime = calendar.DateTime

    return
