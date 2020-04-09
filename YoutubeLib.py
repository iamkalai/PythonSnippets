import bs4 as bs
import requests
import sqlite3

def comparelocalandyoutubelist(url):
    currentSongs = readyoutubeplaylist(url)
    existingSongs = readlocalyoutubelist()
    difflist(existingSongs, currentSongs)


def difflist(li1, li2):
    return (list(set(li1) - set(li2)))


def resetandloadyoutubelisttolocal(url):
    load_success = False
    sqlite_insert_query = """INSERT INTO `videos` ('title', 'url', 'type') VALUES (? , ? , ?);"""
    sqlite_delete_query = """DELETE from videos"""
    try:
        r = requests.get(url)

        soup = bs.BeautifulSoup(r.content, 'html.parser')
        songs = soup.find('ol', attrs={'class': 'playlist-videos-list yt-uix-scroller yt-viewport'})

        sqlite_connection = sqlite3.connect('Youtube')
        cursor = sqlite_connection.cursor()
        cursor.execute(sqlite_delete_query)
        for song in songs.find_all('li'):
            data_tuple = (song.div.h4.text.strip(), song.a['href'], 'Songs')
            cursor.execute(sqlite_insert_query, data_tuple)

        sqlite_connection.commit()
        load_success = True
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
    return load_success


def readlocalyoutubelist():
    songs = []
    try:
        sqlite_connection = sqlite3.connect('Youtube')
        cursor = sqlite_connection.cursor()

        sqlite_select_query = """SELECT title from videos ORDER BY title ASC"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()

        for row in records:
            songs.append(row[0])

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
    return songs


def readyoutubeplaylist(url):
    current_songs = []

    r = requests.get(url)
    soup = bs.BeautifulSoup(r.content, 'html.parser')
    songs = soup.find('ol',attrs= {'class':'playlist-videos-list yt-uix-scroller yt-viewport'})

    for song in songs.find_all('li'):
        current_songs.append(song.div.h4.text.strip())

    current_songs.sort()
    return current_songs

url = "https://www.youtube.com/watch?v=f7UpNvsy8G8&list=PLOuq5xjfqtWKvFoAa68WdWMeUiAOmO_Fb"
# current_songs = readyoutubeplaylist(url)
# for song in current_songs:
#    print(song)

# current_songs = readlocalyoutubelist()
# for song in current_songs:
#     print(song)

# print(resetandloadyoutubelisttolocal(url))

missing_songs = comparelocalandyoutubelist(url)
if(missing_songs is not None):
    print("Missing songs are\n")
    for song in missing_songs:
        print(song)
else:
    print("No songs has changed")

