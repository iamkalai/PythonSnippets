#read chrome bookmarks URL only

from bs4 import BeautifulSoup
file = open("bookmarks_17_06_2018.html", "r")
soup = BeautifulSoup(file, "html.parser")
urls = soup.find_all('a')
for url in urls:
	print(url['href'])