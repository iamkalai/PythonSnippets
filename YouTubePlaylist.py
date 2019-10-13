import bs4 as bs
import requests
import sqlite3

def readSqliteTable():
    songs = []
    try:
        sqliteConnection = sqlite3.connect('Youtube')
        cursor = sqliteConnection.cursor()

        sqlite_select_query = """SELECT title from videos"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()

        for row in records:
            songs.append(row[0])

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            return songs

def Diff(li1, li2):
	return (list(set(li1) - set(li2)))

print("Please wait till we process the request.. \n")
currentSongs = []
existingSongs = readSqliteTable()

url = "https://www.youtube.com/watch?v=f7UpNvsy8G8&list=PLOuq5xjfqtWKvFoAa68WdWMeUiAOmO_Fb"
r = requests.get(url)

soup = bs.BeautifulSoup(r.content, 'html.parser')
songs = soup.find('ol',attrs= {'class':'playlist-videos-list yt-uix-scroller yt-viewport'})

for song in songs.find_all('li'):
    currentSongs.append(song.div.h4.text.strip())

print(Diff(existingSongs , currentSongs))


