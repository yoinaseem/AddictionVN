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


label start:

    show screen calendar_screen
    show screen map_screen
    call variables
    $ Output = calendar.Output

    $ GameRunning = True
    while GameRunning:

        $ Location_img = Location.lower()
        if renpy.has_image(Location_img, exact=True):
            scene expression Location_img

        "Hmmm there's not much to do right now..."

        if Location == "Dorm":
            call dorm_script

        if Location == "Bedroom":
            scene bedroom
            menu:
                "Go to sleep":  
                    $ calendar.AdvanceTime(10)
                    "Wow, I still feel tired."

        # menu:
            # $ MapMenu = renpy.call_screen("MapScreen", _layer="screens")

            # "hello":
            #     "hi"
            # "Open map":
                # $ Location = renpy.call_screen("MapScreen", _layer="screens")
    return

    #call introscript


label dorm_script:
    scene dorm
    show demo     
    r1 "Hey [PLAYERNAME]!"
    r1 "Wanna go outside on a walk with me?"
    menu:
        "Sure, let's go check out campus":
            call college_dialogue
        "Lets take a walk on the streets":
            call street_dialogue
        "Follow me to my room":
            call bedroom_dialogue_r1
        "No I think I'll pass":
            show demo worried
            r1 "Do you not like me?"
    return

label bedroom_dialogue_r1:
    $ Location = "Bedroom"
    scene bedroom
    show demo happy
    r1 "We're in your bedroom [PLAYERNAME]"
    show demo worried
    r1 "I... I think I'm going to leave..."
    $ calendar.AdvanceTime(1)
    return

label college_dialogue:
    $ Location = "College"
    scene college
    show demo happy at right
    r1 "Wow, campus sure is pretty!"
    m "Yeah. Should we head back?"
    r1 "Yeah."
    $ calendar.AdvanceTime(4)
    $ Location = "Bedroom"
    return

label street_dialogue:
    scene street
    $ Location = "Street"
    show demo worried at right
    r1 "I wonder if there's any street food places nearby..."
    m "Probably not."
    r1 "Let's just get back home, I'm hungry."
    $ calendar.AdvanceTime(4)
    $ Location = "Bedroom"
    return

label variables:

    $ PLAYERNAME = "Anon"
    $ calendar = Calendar(
        ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], 
        ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], 
        [31, 28,31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        ["Morning", "Afternoon", "Evening", "Night"],
        8,
        0,
        0,
        0,
        0
        )
    return

label OpenMap:

    $ Location = renpy.call_screen("MapScreen", _layer="screens")
    #call screen MapScreen
    return

# label introscript:

#     scene tokyo_street

#     "Last month I got my acceptance letter from the College of Winterhold."

#     "To be honest I don't know if I want to be here. I'm not sure I'm ready for this kind of responsibility."

#     "I wonder what kind of people my flatmates are." 

#     "Hopefully my flatmates turn out to be chill people."

#     scene school_hallway

#     "Well, this is it. Here we are."

#     "There's no turning back now."  
    
#     "I have to get to the dorms now"
    
#     "Hmm I wonder where that is though.."
    
#     #"Hitting sfx"
    
#     show joker download:
#         xalign 0.5
#         yalign 0.5
    
#     h "I shall defeat you vile serpent"
    
#     m "Wait wha.."
    
#     h "YOU CAN TALK!?"
    
#     h "Guess you're not a serpent after all!"
    
#     m "I.."
    
#     h "Look over there!" 
    
#     h "There are more creatures that need slaying there"
    
#     m "More of what" 
    
#     m "Wait are you a student here"
    
#     m "Do you know how to..."
    
#     h "IT IS TIME TO VANQUISH THE EVIL"
    
#     m "...get to the dorms?" 
    
#     hide joker download 

#     "She just ran off..." 
    
#     h "Dorms are to your right"
    
#     m "Oh."
    
#     m "Thanks." 
    
#     "What. The. Actual. Fuck"
    
#     "Well lets see if her directions were right"
    
#     scene house_bedroom

#     show roommate1pic
#     r1 "Hey how're you doing?"

#     m "I'm alright man, my name is [PLAYERNAME]"

#     r1 "I'm roommate 1"

#     show roommate2pic
#     r2 "I'm roommate 2"

#     show roommate3pic
#     r3 "I'm roommate 3"

#     show roommate1pic
#     r1 "Come on, we'll get acquainted after you hit this bowl"

#     m "Huh? I don't smoke"

#     show roommate2pic
#     r2 "That's not how it is in college bro trust, you'll change your mind just hit it"

#     m "Fuck it let's do it"
#     hide roommate2pic

#     "Here goes nothing..."

#     call EventCheck

#     return
