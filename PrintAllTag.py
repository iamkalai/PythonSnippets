# read the song name from tags and renames the file name as same

import os
from mutagen.id3 import ID3

rootdir = '/media/kp/165DAB2F3112DA16/S_Test/Test'

i = 0
error = 0
for subdir, dirs, files in os.walk(rootdir):

    for file in files:
        try:
            audio = ID3(os.path.join(subdir, file))
            print(file + '-' + audio.pprint())
            #audio.save()
            i = i + 1

        except:
            error = error + 1
            print(file + " With Error")

print(i)
print(error)
