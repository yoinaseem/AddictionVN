label start:

    call variables

    $ DateTime = calendar.DateTime

    $ GameRunning = True
    while GameRunning:
        window hide
        $ clickType = ""
        $ UIreturn = renpy.call_screen("Main_UI", _layer="screens")

        if clickType == "Nav":
            $ Location = UIreturn

        if clickType == "cheat":
            $ MC.cash += 100


    return
