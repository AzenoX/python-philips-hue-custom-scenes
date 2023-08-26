import time
import _lamps as lamps


def state_save(b):
    for i in lamps.all_list:
        lamps.backups[i] = b.get_light(i)


def state_restore(b, delay=0):
    time.sleep(delay)

    for index, lmp in lamps.backups.items():
        b.set_light(index, lmp['state'])
