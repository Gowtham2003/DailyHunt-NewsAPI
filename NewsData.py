# Coded By Gowtham on 30/05/2020
# Coded Using Vim Text Editor
import requests
import json
from bs4 import BeautifulSoup as bs
from genUrl import getUrl


def paraParse(newsContent):
    soup = bs(newsContent, "lxml")
    pTags = soup.findAll("p")
    cont = ""
    for i in range(len(pTags)):
        cont = cont + pTags[i].text + "\n"
    return cont.strip()


def newsData(query):
    newsDictionary = {
        'success': True,
        'data': []
    }
    URL = getUrl(query)

    responseDict = json.loads(requests.get(URL).content)
    rows = responseDict["data"]["rows"]

    for row in rows:
        try:
            title = row["title"]
        except:
            title = ""
        try:
            url = row["shareUrl"]
        except:
            url = ""
        try:
            contentImage = row["contentImage"]
        except:
            contentImage = ""
        try:
            ImageUrl = contentImage["url"]
        except:
            ImageUrl = ""
        try:
            counter = row["counter"]
        except:
            counter = ""
        try:
            PublishedDt = counter["ingestionDate"]
        except:
            PublishedDt = ""
        try:
            viewCount = counter["viewsCount"]
        except:
            viewCount = ""
        try:
            newsContent = row["content"]
            content = paraParse(newsContent)
        except:
            newsContent = ""
            content = ""
        try:
            publisherStory = row["publisherStoryUrl"]
        except:
            publisherStory = ""

        newsObject = {
            'title': title,
            'imageUrl': ImageUrl,
            'url': url,
            'content': content,
            'PublishedTime': PublishedDt,
            'viewCount': viewCount,
            'publisherStory': publisherStory
        }

        newsDictionary['data'].append(newsObject)

    return newsDictionary
