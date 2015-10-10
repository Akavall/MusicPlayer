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
    return eyed3.load("06 Wonderful, Amazing.mp3").info.time_secs

print "Will play: {}".format(sys.argv[1:])

for file_name in sys.argv[1:]:
    if file_name.split(".") == "wav":
        logging.info("Now playing: {}".format(file_name))
        duration = get_wav_duration(file_name)
        os.system("gnome-open {}".format(file_name))
        time.sleep(duration + 1)
    elif file_name.split(".") == "mp3":
        logging.info("Now playing: {}".format(file_name))
        duration = get_mp3_duration(file_name)
        os.system("gnome-open {}".format(file_name))
        time.sleep(duration + 1)
        
