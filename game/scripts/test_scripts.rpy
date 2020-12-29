label dorm_script:
    scene dorm
    show demo     
    r1 "Hey [MC.name]!"
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


