# MusicPlayer
A simple tool that allows you to play music from a given file

For more convenent usage add this line to `.bashrc` file.

```
alias play_list='python ~/MusicPlayer/play_list.py'
```

Then from your music library directory call:

```
play_list "my_song_1.mp3" "my_song_2.wav"
```

To play songs of one artist:


Add this line to you `.bashrc` file:
```
alias play_artist='python ~/MusicPlayer/play_artist.py'
```

Then from your music library directory call:
```
play_artist "~/MyMusicLibrary" "my_favorite_artist"
``` 

*Create a Custom play list*

create a play_list file:
my_play_list.txt
```
my_song_1.wav
my_song_2.wav
my_song_n.wav
```

call it:
```
play_list `cat my_play_list.txt`
```