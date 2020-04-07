import bs4 as bs
import requests
import sqlite3

url = "https://www.youtube.com/watch?v=f7UpNvsy8G8&list=PLOuq5xjfqtWKvFoAa68WdWMeUiAOmO_Fb"
sqlite_insert_query = """INSERT INTO `videos` ('title', 'url', 'type') VALUES (? , ? , ?);"""
sqlite_delete_query = """DELETE from videos"""
try:
    print("Please wait till we process the request.. \n")
    r = requests.get(url)

    soup = bs.BeautifulSoup(r.content, 'html.parser')
    songs = soup.find('ol', attrs={'class': 'playlist-videos-list yt-uix-scroller yt-viewport'})

    sqliteConnection = sqlite3.connect('Youtube')
    cursor = sqliteConnection.cursor()
    cursor.execute(sqlite_delete_query)
    for song in songs.find_all('li'):
        data_tuple = (song.div.h4.text.strip(), song.a['href'], 'Songs')
        count = cursor.execute(sqlite_insert_query, data_tuple)

    sqliteConnection.commit()
    print("YouTube playlist loaded successfully")
    cursor.close()

except sqlite3.Error as error:
    print("Failed to insert data into sqlite table", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()

