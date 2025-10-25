transform right_stay:
    zoom 0.6
    right
    ypos 1.25

transform half_size:
    zoom 0.5

transform right_sit:
    zoom 0.5
    right
    xalign 0.82
    yalign 2.3

transform train_sway:
    truecenter
    linear 0.3 xoffset 0 yoffset 2
    linear 0.3 xoffset 2 yoffset -2
    linear 0.3 xoffset 0 yoffset 2
    linear 0.3 xoffset -2 yoffset -2 
    repeat

transform shake:
    truecenter
    linear 0.05 xoffset -20 yoffset -20 
    linear 0.05 xoffset 20 yoffset 20 
    linear 0.05 xoffset -20 yoffset 20 
    linear 0.05 xoffset 0 yoffset 0 
    reset