screen ClickyScreen():
    for q in ClickObjects:
        if q.location == Location and q.isActive:
            imagebutton: 
                hover q.Icon
                idle q.Icon
                focus_mask True
                hovered tt.Action(q.name)
                action SetVariable("clickType", q.clickType), Return(q.Clicked)

        if clickType == "Object" or clickType == "Character" or clickType == "Map":
            if q.location == Location and q.isActive:
                imagebutton: 
                    hover q.Icon
                    idle q.Icon
                    focus_mask True
                    action NullAction()


