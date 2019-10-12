#read the song name from tags and renames the file name as same

import os
from mutagen.id3 import ID3, APIC;
from mutagen.easyid3 import EasyID3

path = '/media/kp/165DAB2F3112DA16/S_Test/Songs/English'
files = os.listdir(path)
i = 0
error = 0

for file in files:
    try:
        #audio = EasyID3(os.path.join(path, file))
        #print(os.path.join(path, file))
        #print(audio['artist'])
        audio = ID3(os.path.join(path, file))

        with open('logo.jpg', 'rb') as albumart:
            audio['APIC'] = APIC(
                encoding=3,
                mime='image/jpeg',
                type=3,
                desc=u'Cover',
                data=albumart.read()
            )

        audio.save()
        i = i+1
    except:
        error = error + 1
        print (file + " With Error")

print(i)
print(error)


