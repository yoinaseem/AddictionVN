screen CharacterScreen():
    for q in Characters:
        if q.isActive and q.isLocal:
            imagebutton: 
                    hover q.Avatar
                    idle q.Avatar
                    focus_mask True
                    action SetVariable("clickType", "Character"), Return(q.cfname)
                    hovered tt.Action(q.FullName) 

        if navMenu:
            if q.isActive and q.isLocal:
                imagebutton: 
                        hover q.Avatar
                        idle q.Avatar
                        focus_mask True
                        action NullAction()