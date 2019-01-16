from collections import OrderedDict
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from youtube_dl import YoutubeDL

url = "https://www.apple.com/itunes/charts/songs/"
conn = urlopen(url)
raw_data = conn.read()
content = raw_data.decode("utf8")
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

    options = {
        "default_search": "ytsearch",
        "max_download": 1,
        "format": "bestaudio/audio"
    }
    dl = YoutubeDL(options)
    dl.download([song_name, "-", artist])
