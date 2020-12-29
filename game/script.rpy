define p = Character("Psychadelic")
define s = Character("Stimulant")
define d = Character("Dissociative")
define ad = Character("Anti-Depressant")
define o = Character("Opioids")
define h = Character ("Hallucinogens")
define r1 = Character("Roommate1")
define r2 = Character("Roommate2")
define r3 = Character("Roommate3")
define m = Character("Me")

default Location = "Bedroom"
default BGImage = ""

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

        $ Location_img = Location.lower()
        if renpy.has_image(Location_img, exact=True):
            scene expression Location_img

        "Hmmm there's not much to do right now..."
        $ clickType = ""


        if Location == "Dorm":
            call dorm_script

        if Location == "Bedroom":
            scene expression "bedroom"
            menu:
                "Go to sleep":  
                    $ calendar.AdvanceTime(10)
                    "Wow, I still feel tired."

    return


