# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
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

    "There's no turning back now.:c"

    return
