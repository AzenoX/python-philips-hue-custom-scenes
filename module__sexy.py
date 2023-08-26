import time
import _colors as colors
import _lamps as lamps
import _utils as ut


def sexy_room(b, room, count, speed=0.05, ghome=None):
    if ghome:
        ghome.play('https://azenox.fr/sounds/whisper.mp3')

    time.sleep(0.2)

    ut.turn_all_on(b, room)

    if count == 'Infinite':
        while True:
            run_loop(b, room, speed)
    else:
        for i in range(count):
            run_loop(b, room, speed)


def run_loop(b, room, speed=0.05):
    current_colors = [
        colors.light_purple,
        colors.purple,
        colors.light_pink,
        colors.pink,
        colors.deep_pink,
    ]
    for c in current_colors:  # Add a step to loop some kind, faster
        for x in range(len(lamps.all[room])):
            b.set_light(lamps.all[room][x], 'hue', c)
            time.sleep(speed)
