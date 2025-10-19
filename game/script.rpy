init python:
    renpy.music.register_channel("bgs", "sfx", loop = True)

# Игра начинается здесь:
label start:
    jump station
    
    return