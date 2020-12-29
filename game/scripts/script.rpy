label start:

    call variables

    # show screen calendar_screen
    # show screen map_screen
    # $ Output = calendar.Output
    # $ Location_img = Location.lower()
    
    # if renpy.has_image(Location_img, exact=True):
    #     scene expression Location_img

    # $ Location_img = Location.lower()
    # if renpy.has_image(Location_img, exact=True):
    #     scene expression Location_img

    # "Hmmm there's not much to do right now..."

    # if Location == "Dorm":
    #         call dorm_script

    # if Location == "Bedroom":
    #     scene bedroom
    #     menu:
    #         "Go to sleep":  
    #             $ calendar.AdvanceTime(10)
    #             "Wow, I still feel tired."

    # jump start

    $ GameRunning = True
    while GameRunning:
        # $ UIreturn = renpy.call_screen("Main_UI")
        show screen calendar_screen
        show screen map_screen
        $ Output = calendar.Output

        # $ Location_img = Location.lower()
        # if renpy.has_image(Location_img, exact=True):
        #     scene expression Location_img

        # "Hmmm there's not much to do right now..."
        # $ clickType = ""

        menu:
            "[MC.name]: Strength: [MC.strength], Charm: [MC.charm], Cash: [MC.cash]"
            "Add Cash":
                $ MC.cash += 100
            "Train Strength":
                $ MC.strength += 1
            "Increase Charm":
                $ MC.charm += 1
             

        # if Location == "Dorm":
        #     call dorm_script

        # if Location == "Bedroom":
        #     scene expression "bedroom"
        #     menu:
        #         "Go to sleep":  
        #             $ calendar.AdvanceTime(10)
        #             "Wow, I still feel tired."

    return


