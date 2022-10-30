''' a program for downloading the mp3 '''
from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Title : ", yt.title)

print("Views : ", yt.views)

audio = yt.streams.get_audio_only()

audio.download("/home/pixure/Music")