#%% [markdown]
# # Use this script to download all the lectures for "Practical Data Science"

#%%
import feedparser
import os
import requests
import shutil
from urllib.request import urlretrieve

RSS_ADDRESS = r"http://scs.hosted.panopto.com/Panopto/Podcast/Podcast.ashx?courseid=912b80a3-625d-405d-8905-a8620133666b&type=mp3"

d = feedparser.parse(RSS_ADDRESS)

#%%
os.mkdir("videos")


#%%
def download_file(url, newname):
    local_filename = newname
    with requests.get(url, stream=True) as r:
        with open(local_filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

    return local_filename

for each in d["entries"][13:]:
    newname = r"videos/" + each.title.replace(" ","_").replace(":","").replace("-","_").replace(r"/","_") + ".mp4"
    url = each.link
    print(newname)
    print(url)
    download_file(url, newname)



#%%
