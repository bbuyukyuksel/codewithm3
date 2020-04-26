#python3.7.4
#pip install beautifulsoup4
#pip install pytube3
#pip install -U mechanize

import codecs
from bs4 import BeautifulSoup
from pytube import YouTube
import mechanize
import os
import time

# Read video titles from .txt file
with codecs.open('Play List.txt', 'r', 'utf-8') as f:
    queries = list(filter(lambda x: x, f.read().replace('\r', '').split('\n')))

website = 'https://www.youtube.com'

# Save Directory
output_path = 'Downloads'
os.makedirs(output_path, exist_ok=True)

# Start mechanize browser
br = mechanize.Browser()
br.set_handle_equiv(False)
br.set_handle_robots(False)
br.set_handle_referer(False)
br.set_handle_refresh(False)
br.open(website)

# Parse HTML contents and download.
for index, query in enumerate(queries):
    print("{:<3} Preparing to download: {}".format(index+1, query))
    br.select_form(nr=1)
    br.form["search_query"] = query
    br.submit()
    time.sleep(2)
    print("\tFound >>", br.title())
    source = BeautifulSoup(br.response().read(), features="html5lib")
    links = source.find_all('div', attrs={'class': 'yt-lockup-thumbnail'})
    video_link = links[0].a.get('href')  
    full_video_link = website + video_link
    print("\tDownloading from", website + video_link)
    video = YouTube(full_video_link)
    ##print(video.streams.filter(file_extension = "mp4").all)
    video.streams.get_by_itag(18).download(output_path=output_path)
