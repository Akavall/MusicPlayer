import wave
import contextlib
import os
import time
import sys
import logging
import eyed3

logging.getLogger().setLevel(logging.INFO)

def get_wav_duration(file_name):
    with contextlib.closing(wave.open(file_name,'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        return duration

def get_mp3_duration(file_name):
    return eyed3.load(file_name).info.time_secs


def play_wav(file_name):
    logging.info("Now playing: {}".format(file_name))
    duration = get_wav_duration(file_name)
    os.system("gnome-open \"{}\"".format(file_name))
    time.sleep(duration + 1)
    
def play_mp3(file_name):
    logging.info("Now playing: {}".format(file_name))
    duration = get_mp3_duration(file_name)
    os.system("gnome-open \"{}\"".format(file_name))
    time.sleep(duration + 1)
