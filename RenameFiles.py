#os.rename(os.path.join(path, file), os.path.join(path, songTitle + '.mp3'))



# read the song name from tags and renames the file name as same

import os

rootdir = '/media/kp/165DAB2F3112DA16/S_Test/Songs'

i = 0
error = 0
for subdir, dirs, files in os.walk(rootdir):

    for file in files:
        try:
            filename = os.path.splitext(file)[0]
            #print(filename.title())
            os.rename(os.path.join(subdir, file), os.path.join(subdir, filename.title() + '.mp3'))
            #print(file)
            i = i + 1

        except:
            error = error + 1
            print(file + " With Error")

print(i)
print(error)
