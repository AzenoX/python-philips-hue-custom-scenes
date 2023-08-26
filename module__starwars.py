import time
import _utils as ut
import _rooms as rooms
import _colors as colors


def pewpew(b, room):
    ut.set_all_brightness(b, room, 0)
    ut.set_all_color(b, room, colors.yellow)
    ut.turn_all_off(b, room)
    ut.turn_all_on(b, room)

    for i in range(5):
        time.sleep(0.6)
        ut.turn_all_on(b, room)
        ut.set_all_brightness(b, room, 150)
        ut.set_all_color(b, room, colors.yellow)
        time.sleep(0.1)
        ut.turn_all_off(b, room)
