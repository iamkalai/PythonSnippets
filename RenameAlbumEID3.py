# read the song name from tags and renames the file name as same

import os
from mutagen.easyid3 import EasyID3

rootdir = '/media/kp/165DAB2F3112DA16/S_Test/Songs'

i = 0
error = 0
for subdir, dirs, files in os.walk(rootdir):

    for file in files:
        try:
            audio = EasyID3(os.path.join(subdir, file))
            audio['album'] = os.path.basename(subdir)
            if("unknown" in str(audio['artist'])):
                audio['artist'] = ''
            if ("www." in str(audio['artist'])):
                audio['artist'] = ''
            if (".com" in str(audio['artist'])):
                audio['artist'] = ''
            if ("music" in str(audio['artist'])):
                audio['artist'] = ''
            if ("artist" in str(audio['artist'])):
                audio['artist'] = ''
            if ("VARIOUS" in str(audio['artist'])):
                audio['artist'] = ''
            audio['albumartist'] = audio['artist']
            audio['composer'] = ''

            audio['tracknumber'] = ''
            audio['discnumber'] = ''
            audio['date'] = ''
            audio['originaldate'] = ''
            audio['media'] = ''
            audio['author'] = ''
            audio['lyricist'] = ''
            audio['arranger'] = ''
            audio['performer'] = ''
            audio['website'] = ''
            audio['encodedby'] = ''
            audio['genre'] = ''
            audio['copyright'] = ''
            audio['isrc'] = ''

            audio.save()
            i = i + 1

        except:
            error = error + 1
            print(file + " With Error")

print(i)
print(error)
