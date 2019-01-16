from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict
import pyexcel
# urllib
url = "https://dantri.com.vn"
# 1. Download the page

# 1.1 Open connection ( mo ket noi)
conn = urlopen(url)

# 1.2 Read data (doc du lieu)
raw_data = conn.read()

# 1.3 Decode data (giai ma du lieu)
content = raw_data.decode("utf8")

########################################## tao trang moi in ra dantri.html
# f = open("dantri.html", "wb")
# f.write(raw_data)
# f.close()
##########################################
# 2. Find ROI 
soup = BeautifulSoup(content, "html.parser") # bat soup to
ul_new = soup.find("ul", "ul1 ulnew") # id = "data-port" #bat soup be

                                #find : tra ve 1 soup
                                #find_all : tra ve 1 list
# 3. Copy and Save
li_list = ul_new.find_all("li")
# li = li_list[0] 
news_list = []
for li in li_list:
    #walking
    h4 = li.h4
    a = h4.a
    link = url + a["href"]
    title = a.string
    # print(link, title)
    # print("------------------")
    news = OrderedDict({
        "title": title,
        "link": link
    })
    news_list.append(news)
pyexcel.save_as(records=news_list, dest_file_name="dantri.xlsx")