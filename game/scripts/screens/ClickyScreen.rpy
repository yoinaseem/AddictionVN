screen ClickyScreen():
    for q in ClickObjects:
        if q.location == Location:
            if q.isActive:
                imagebutton: 
                    hover q.Icon
                    idle q.Icon
                    focus_mask True
                    action SetVariable("clickType", q.clickType), Return(q.Clicked)
                    hovered tt.Action(q.name)