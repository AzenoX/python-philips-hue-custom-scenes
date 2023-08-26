import os

from phue import Bridge
import time
import pyaudio
from dotenv import load_dotenv

import _rooms as rooms
import _lamps as lamps

import _utils as ut

import module__starwars as m_sw
import module__test as m_test
import module__police as m_police

load_dotenv()

# Variables
INPUT_INDEX = 1
CHANNELS = 1
FRAME_RATE = 48000
RECORD_SECONDS = 6
AUDIO_FORMAT = pyaudio.paInt16
SAMPLE_SIZE = 2

# Queues
# messages = Queue()
# recordings = Queue()

# Model
# model = Model(model_name="vosk-model-fr-0.22")
# rec = KaldiRecognizer(model, FRAME_RATE)
# rec.SetWords(True)


# def start_recording():
#     messages.put(True)
#
#     record = Thread(target=record_microphone)
#     record.start()
#
#     transcribe = Thread(target=speech_recognition)
#     transcribe.start()
#
#
# def stop_recording():
#     messages.get()
#
#
# def record_microphone(chunk=1024):
#     p = pyaudio.PyAudio()
#     stream = p.open(format=AUDIO_FORMAT, channels=CHANNELS, rate=FRAME_RATE, input=True, input_device_index=INPUT_INDEX,
#                     frames_per_buffer=chunk)
#     frames = []
#
#     while not messages.empty():
#         data = stream.read(chunk)
#         frames.append(data)
#
#         if len(frames) >= (FRAME_RATE * RECORD_SECONDS) / chunk:
#             recordings.put(frames.copy())
#             frames = []
#
#     stream.stop_stream()
#     stream.close()
#     p.terminate()
#
#
# def speech_recognition():
#     while not messages.empty():
#         frames = recordings.get()
#         rec.AcceptWaveform(b''.join(frames))
#         result = rec.Result()
#         text = json.loads(result)["text"]
#         print(text)


# def detections(text):
#     if "star wars" in text | "starwars" in text:
#         scene__star_wars()


def state_save():
    for i in lamps.all_list:
        lamps.backups[i] = b.get_light(i)


def state_restore(delay=0):
    time.sleep(delay)

    for index, lmp in lamps.backups.items():
        b.set_light(index, lmp['state'])


if __name__ == '__main__':
    # ut.list_devices()

    b = Bridge(os.getenv('BRIDGE_IP'))

    # If the app is not registered and the button is not pressed, press the button and call connect()
    b.connect()

    # Save state before doing anything

    state_save()

    # Start recording
    # start_recording()

    # m_sw.pewpew(b, rooms.SALON)
    m_police.pin_pon(b, rooms.SALON, 10)
    # m_test.loop_colors(b, rooms.SALON, 2, 3)

    state_restore(delay=2)
