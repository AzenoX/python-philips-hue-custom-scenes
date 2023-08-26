import _lamps as lamps
import pyaudio


def turn_all_on(b, room, transitiontime=0):
    b.set_light(lamps.all[room], 'on', True, transitiontime=transitiontime)


def turn_all_off(b, room, transitiontime=0):
    b.set_light(lamps.all[room], 'on', False, transitiontime=transitiontime)


def set_all_color(b, room, color, transitiontime=0):
    b.set_light(lamps.all[room], 'hue', color, transitiontime=transitiontime)


def set_all_brightness(b, room, brightness, transitiontime=0):
    b.set_light(lamps.all[room], 'bri', brightness, transitiontime=transitiontime)


def list_devices():
    p = pyaudio.PyAudio()
    for i in range(p.get_device_count()):
        print(p.get_device_info_by_index(i))
    p.terminate()
