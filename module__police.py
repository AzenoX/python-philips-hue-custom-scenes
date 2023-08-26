import time
import _colors as colors
import _lamps as lamps
import _utils as ut


def pin_pon(b, room, count):
    ut.turn_all_on(b, room)

    if count == 'Infinite':
        while True:
            run_loop(b, room)
    else:
        for i in range(count):
            run_loop(b, room)


def run_loop(b, room):
    current_colors = [
        colors.red,
        colors.blue
    ]
    for c in current_colors:  # Add a step to loop some kind, faster
        for x in range(len(lamps.all[room])):
            b.set_light(lamps.all[room][x], 'hue', c)
            time.sleep(0.05)
