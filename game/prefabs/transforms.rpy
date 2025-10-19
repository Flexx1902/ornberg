transform left_inset:
    xalign 0.1   # от левого края
    yalign 1.0    # по нижнему краю 

transform right:
    xalign 1.0   # от прав края
    yalign -1.0    # по нижнему краю

transform normal_size:
    zoom 0.6

transform half_size:
    zoom 0.5    # 50% от оригинала

transform sit_position:
    xalign 0.82
    yalign 2.0

transform train_sway:
    zoom 1.003
    linear 0.3 yoffset -4 xoffset -4
    linear 0.3 yoffset 0 xoffset 0
    linear 0.3 yoffset -2 xoffset -4
    repeat