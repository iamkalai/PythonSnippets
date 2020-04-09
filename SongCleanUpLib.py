import os
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, APIC


def renamesongsalbum(path, name):
    # read the songs and rename its album name
    files = os.listdir(path)
    i = 0
    error = 0

    for file in files:
        try:
            audio = EasyID3(os.path.join(path, file))
            audio['album'] = name
            audio.save()

            i = i + 1
        except:
            error = error + 1
            print(file + " errored")

    print("Number of files processed successfully:" + str(i))
    print("Number of files that errored out:" + str(error))


def changesongsalbumart(path, imageName):
    # read the songs and change its album art
    files = os.listdir(path)
    i = 0
    error = 0

    for file in files:
        try:
            audio = ID3(os.path.join(path, file))

            with open(imageName, 'rb') as albumart:
                audio['APIC'] = APIC(
                    encoding=3,
                    mime='image/png',
                    type=3,
                    desc=u'Cover',
                    data=albumart.read()
                )

            audio.save()
            i = i + 1
        except:
            error = error + 1
            print(file + " errored")

    print("Number of files processed successfully:" + str(i))
    print("Number of files that errored out:" + str(error))


def resetsongsusingeid3(path):
    # read the songs and reset all the tags
    i = 0
    error = 0
    for subdir, dirs, files in os.walk(path):

        for file in files:
            try:
                audio = EasyID3(os.path.join(subdir, file))
                audio['album'] = os.path.basename(subdir)
                if ("unknown" in str(audio['artist'])):
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
                print(file + " errored")

    print("Number of files processed successfully:" + str(i))
    print("Number of files that errored out:" + str(error))


def resetsongsusingid3(path):
    # read the songs and reset all the tags using ID3
    i = 0
    error = 0
    for subdir, dirs, files in os.walk(path):

        for file in files:
            try:
                audio = ID3(os.path.join(subdir, file))
                audio.delall('APIC')
                audio.delall('TCAT')
                audio.delall('TDES')
                audio.delall('TGID')
                audio.delall('WFED')
                audio.delall('COMM')
                audio.delall('MCDI')
                audio.delall('MLLT')
                audio.delall('OWNE')
                audio.delall('SYLT')
                audio.delall('TCOM')
                audio.delall('TCOP')
                audio.delall('TDOR')
                audio.delall('TDRC')
                audio.delall('TDRL')
                audio.delall('TDTG')
                audio.delall('TENC')
                audio.delall('TEXT')
                audio.delall('TIPL')
                audio.delall('TIT1')
                audio.delall('TIT3')
                audio.delall('TKEY')
                audio.delall('TLAN')
                audio.delall('TMCL')
                audio.delall('TMOO')
                audio.delall('TCON')
                audio.delall('TSO2')
                audio.delall('TSOC')
                audio.delall('UFID')

                audio.delall('PRIV')
                audio.delall('TSSE')
                audio.delall('TBPM')

                audio.delall('TOAL')
                audio.delall('TOFN')
                audio.delall('TOLY')
                audio.delall('TOPE')
                audio.delall('TOWN')
                audio.delall('TPE2')
                audio.delall('TPE3')
                audio.delall('TPE4')
                audio.delall('TPOS')
                audio.delall('TPRO')
                audio.delall('TPUB')
                audio.delall('TRCK')
                audio.delall('TRSN')
                audio.delall('TRSO')
                audio.delall('TSOA')
                audio.delall('TSOP')
                audio.delall('TSOT')
                audio.delall('TSST')
                audio.delall('TXXX')
                audio.delall('USER')
                audio.delall('USLT')
                audio.delall('WCOM')
                audio.delall('WCOP')
                audio.delall('WOAF')
                audio.delall('WOAR')
                audio.delall('WOAS')
                audio.delall('WORS')
                audio.delall('WPAY')
                audio.delall('WPUB')
                audio.delall('WXXX')
                print(audio.pprint())
                audio.save()
                i = i + 1

            except:
                error = error + 1
                print(file + " errored")

    print("Number of files processed successfully:" + str(i))
    print("Number of files that errored out:" + str(error))


def renamefilesasmp3(path):
    # read and rename all the files as mp3
    i = 0
    error = 0
    for subdir, dirs, files in os.walk(path):

        for file in files:
            try:
                filename = os.path.splitext(file)[0]
                os.rename(os.path.join(subdir, file), os.path.join(subdir, filename.title() + '.mp3'))
                i = i + 1

            except:
                error = error + 1
                print(file + " errored")

    print("Number of files processed successfully:" + str(i))
    print("Number of files that errored out:" + str(error))


def printallsongtags(path):
    i = 0
    error = 0
    for subdir, dirs, files in os.walk(path):

        for file in files:
            try:
                audio = ID3(os.path.join(subdir, file))
                print(file + '-' + audio.pprint())
                i = i + 1

            except:
                error = error + 1
                print(file + " errored")

    print("Number of files processed successfully:" + str(i))
    print("Number of files that errored out:" + str(error))


def renamefileassongname(path):
    # Read the song and rename file as song name
    files = os.listdir(path)
    i = 1

    for file in files:
        try:
            id3Info = ID3(os.path.join(path, file))
            songTitle = (id3Info["TIT2"].text[0])
            os.rename(os.path.join(path, file), os.path.join(path, songTitle + '.mp3'))
            i = i + 1
        except:
            print(file + " errored")
    print("Number of files processed successfully:" + str(i))


path = ''
# renamesongsalbum(path,"English")
# changesongsalbumart(path,"") #pass the full path name of image
# resetsongsusingeid3(path)
# resetsongsusingid3(path)
# renamefilesasmp3(path)
# printallsongtags(path)
# renamefileassongname(path)
