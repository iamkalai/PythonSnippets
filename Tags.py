#read the song name from tags and renames the file name as same

import os
from mutagen.id3 import ID3;

path = 'the path from which the files need to read'
files = os.listdir(path)
i = 1

for file in files:
    try:
        id3Info= ID3(os.path.join(path, file))
        songTitle = (id3Info["TIT2"].text[0])
        os.rename(os.path.join(path, file), os.path.join(path, songTitle + '.mp3'))
        i = i+1
    except:
        print (file + " With Error")
print(i)
