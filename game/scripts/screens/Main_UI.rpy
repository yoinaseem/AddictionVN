screen Main_UI():
    use BGIMAGE
    use top_tbar
    use ClickyScreen
    use CharacterScreen
    if navMenu:
        use NavMap
    use map_icon
    use TipScreen
    if Notification:
        add "ui/Notif.png"


