screen BGIMAGE():
    $ Background = "images/places/backgrounds/dorm.jpg"
    for q in Places:
        if q.name == Location:
            $ Background = q.BG_Image
    add Background
