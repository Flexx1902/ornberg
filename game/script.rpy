init python:
    renpy.music.register_channel("bgs", "sfx", loop = True)
    if "background" not in config.layers:
        config.layers.insert(0, "background")

# Точка входа
label start:
    python:
        renpy.show("black_bg", what=Solid("#000000"), layer="background", zorder=0)

    jump intro_station
    
    return