#read the song name from tags and renames the file name as same

import os
from mutagen.id3 import ID3, APIC
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import EasyMP3

path = '/media/kp/165DAB2F3112DA16/Songs/Cleanup'
files = os.listdir(path)
i = 0
error = 0

for file in files:
    try:
        #audio = EasyID3(os.path.join(path, file))
        #print(os.path.join(path, file))
        #print(audio['artist'])

        audio = EasyID3(os.path.join(path, file))
        audio['album'] = 'English'
        audio.save()

        i = i+1
    except:
        error = error + 1
        print (file + " With Error")

print(i)
print(error)


