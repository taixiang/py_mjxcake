import requests
from bs4 import BeautifulSoup

import os
import django
import time, datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cakesite.settings")
django.setup()
from english.models import learn


# learnEn = learn.objects.get_or_create(time="12-27")

# time1==最新的
def spiderEn():
    response = requests.get("http://m.chinavoa.com/51voa/")
    soup = BeautifulSoup(response.content, "html5lib")
    content = soup.find("dl", class_="block_con").dd.ul
    lilist = content.find_all("li")

    for index, li in enumerate(lilist):
        if "VOA慢速英语" in li.a.contents[1]:
            if li.a.contents[0].string < "12-00":
                time1 = str(datetime.datetime.now().year) +"-"+li.a.contents[0].string
                title = li.a.contents[1][8:]
                learnEn, hasEn = learn.objects.get_or_create(time=time1, title=title)
                if hasEn == 1:
                    learnEn.url = li.a.get("href")
                    detailRep = requests.get(li.a.get("href"))
                    detailSoup = BeautifulSoup(detailRep.content, "html5lib")
                    plist = detailSoup.find("div", class_="neirong").find_all("p")
                    learnEn.audioUrl = detailSoup.find("audio", class_="player").get("m-src")
                    en_content = ""
                    for p in plist:
                        if p.string:
                            en_content = en_content + p.string + "\n"
                    learnEn.content = en_content
                    learnEn.save()

# spiderEn()