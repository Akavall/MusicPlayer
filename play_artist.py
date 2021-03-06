import eyed3
import logging  
import os
import random as rn 
import sys 

from utilities import play_mp3

logging.getLogger().setLevel(logging.INFO)

def get_this_artist_files(current_dir, artist_name):
    all_files = os.listdir(current_dir)
    artist_files = []
    for f in all_files:
        if f[-3:] == "mp3":
            # This only works for mp3 files 
            if eyed3.load(f).tag.artist == artist_name:
                artist_files.append(f)
    return artist_files


artist_files = get_this_artist_files(sys.argv[1], sys.argv[2])

rn.shuffle(artist_files)

logging.info("Found {} files by artist {}".format(len(artist_files), sys.argv[2]))
logging.info("Will play: {}".format(artist_files))

for file_name in artist_files:
    play_mp3(file_name)



        
