# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("Psychadelic")
define s = Character("Stimulant")
define d = Character("Dissociative")
define ad = Character("Anti-Depressant")

define r1 = Character("Roommate1")
define r2 = Character("Roommate2")
define r3 = Character("Roommate3")

define m = Character("Me")


# The game starts here.

label start:

    # { BACKGROUND }
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene tokyo_street
    # { CHARACTER SPRITE }
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    #{ DIALOGUE }
    # These display lines of dialogue.

    "Last month I got my acceptance letter from the College of Winterhold."

    "To be honest I don't know if I want to be here. I'm not sure I'm ready for this kind of responsibility."

    "I wonder what kind of people my flatmates are." 

    "Hopefully my flatmates turn out to be chill people."

    # This ends the game.

    scene school_hallway

    "Well, this is it. Here we are."

    "There's no turning back now.c:"

    scene house_bedroom

    show roommate1pic
    r1 "Hey how're you doing?"

    m "I'm alright man, my name is PLAYERNAME"

    r1 "I'm roommate 1"

    show roommate2pic
    r2 "I'm roommate 2"

    show roommate3pic
    r3 "I'm roommate 3"

    show roommate1pic
    r1 "Come on, we'll get acquainted after you hit this bowl"

    m "Huh? I don't smoke"

    show roommate2pic
    r2 "That's not how it is in college bro trust, you'll change your mind just hit it"

    m "Fuck it let's do it"

    return
