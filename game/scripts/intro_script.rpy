label introscript:

    scene tokyo_street

    "Last month I got my acceptance letter from the College of Winterhold."

    "To be honest I don't know if I want to be here. I'm not sure I'm ready for this kind of responsibility."

    "I wonder what kind of people my flatmates are." 

    "Hopefully my flatmates turn out to be chill people."

    scene school_hallway

    "Well, this is it. Here we are."

    "There's no turning back now."  
    
    "I have to get to the dorms now"
    
    "Hmm I wonder where that is though.."
    
    #"Hitting sfx"
    
    show joker download:
        xalign 0.5
        yalign 0.5
    
    h "I shall defeat you vile serpent"
    
    m "Wait wha.."
    
    h "YOU CAN TALK!?"
    
    h "Guess you're not a serpent after all!"
    
    m "I.."
    
    h "Look over there!" 
    
    h "There are more creatures that need slaying there"
    
    m "More of what" 
    
    m "Wait are you a student here"
    
    m "Do you know how to..."
    
    h "IT IS TIME TO VANQUISH THE EVIL"
    
    m "...get to the dorms?" 
    
    hide joker download 

    "She just ran off..." 
    
    h "Dorms are to your right"
    
    m "Oh."
    
    m "Thanks." 
    
    "What. The. Actual. Fuck"
    
    "Well lets see if her directions were right"
    
    scene house_bedroom

    show roommate1pic
    r1 "Hey how're you doing?"

    m "I'm alright man, my name is [PLAYERNAME]"

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
    hide roommate2pic

    "Here goes nothing..."

    call EventCheck

    return
