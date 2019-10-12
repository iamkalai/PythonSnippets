# read the song name from tags and renames the file name as same

import os
from mutagen.id3 import ID3

rootdir = '/media/kp/165DAB2F3112DA16/Songs/Cleanup'

i = 0
error = 0
for subdir, dirs, files in os.walk(rootdir):

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
            print(file + " With Error")

print(i)
print(error)
