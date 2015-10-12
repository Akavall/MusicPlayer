import sys

from utilities import play_wav, play_mp3    

print "Will play: {}".format(sys.argv[1:])

for file_name in sys.argv[1:]:
    if file_name[-3:] == "wav":
        play_wav(file_name)
    elif file_name[-3:] == "mp3":
        play_mp3(file_name)
