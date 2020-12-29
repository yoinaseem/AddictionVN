screen TipScreen():
    if tt.value <>"":
        frame:
            background None
            xalign 0.5
            ypos 185
            vbox:
                text "[tt.value]"