import bs4 as bs
import requests

print("Please wait till we process the request.. \n")

currentSongs = []
url = "https://www.youtube.com/watch?v=f7UpNvsy8G8&list=PLOuq5xjfqtWKvFoAa68WdWMeUiAOmO_Fb"

r = requests.get(url)
soup = bs.BeautifulSoup(r.content, 'html.parser')
songs = soup.find('ol',attrs= {'class':'playlist-videos-list yt-uix-scroller yt-viewport'})

for song in songs.find_all('li'):
    currentSongs.append(song.div.h4.text.strip())

currentSongs.sort()

print("Total videos:"+str(len(currentSongs)))
print("The videos are \n")
for song in currentSongs:
    print(song)

