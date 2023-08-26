import time
import _colors as colors
import _lamps as lamps
import _utils as ut


def loop_colors(b, room, count, speed=0.2, step=1, ghome=None):
    if ghome:
        ghome.play('https://azenox.fr/sounds/SAX.mp3')

    time.sleep(0.2)

    ut.turn_all_on(b, room)

    if count == 'Infinite':
        while True:
            run_loop(b, room, speed, step)
    else:
        for i in range(count):
            run_loop(b, room, speed, step)


def run_loop(b, room, speed, step=1):
    for c in range(0, len(colors.all), step):  # Add a step to loop some kind, faster
        for x in range(len(lamps.all[room])):
            b.set_light(lamps.all[room][x], 'hue', colors.all[c])
            time.sleep(speed)
