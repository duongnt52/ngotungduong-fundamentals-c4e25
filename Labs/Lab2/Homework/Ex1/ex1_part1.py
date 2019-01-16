from collections import OrderedDict
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = "https://www.apple.com/itunes/charts/songs/"
conn = urlopen(url)
raw_data = conn.read()
content = raw_data.decode("utf8")
# f = open("song.html", "wb")
# f.write(raw_data)
# f.close()
soup = BeautifulSoup(content, "html.parser")
url_new = soup.find("section", "section chart-grid")
li_list = url_new.find_all("li")
new_list = []
for li in li_list:
    h3 = li.h3
    h4 = li.h4
    song_name = h3.string
    artist = h4.string 
    news = OrderedDict({
        "song name": song_name,
        "artist": artist
    })
    new_list.append(news)
pyexcel.save_as(records= new_list, dest_file_name= "Itunes top songs.xlsx")
