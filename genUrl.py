# Coded By Gowtham on 30/05/2020
# Coded Using Vim Text Editor
import requests
from bs4 import BeautifulSoup as bs
import base64


def getUrl(key, language):
    queries = ["science-topics-20", "technology-topics-102", "india-topics-15", "automobile-topics-101", "entertainment-topics-8", "sports-topics-17", "world-topics-16",
               "lifestyle-topics-11", "employment-topics-136", "religion+spirituality-topics-135", "football-topics-495", "movie+review-topics-807", "buzz+trending-topics-791"]

    queryDict = {
        'sci': queries[0],
        'tech': queries[1],
        'ind': queries[2],
        'auto': queries[3],
        'ent': queries[4],
        'spt': queries[5],
        'wrd': queries[6],
        'life': queries[7],
        'emp': queries[8],
        'rel': queries[9],
        'foot': queries[10],
        'mov': queries[11]
    }

    query = queryDict[key]
    url = f"https://m.dailyhunt.in/news/india/{language}/{query}"
    soup = bs(requests.get(url).content, "lxml")
    encodedUrl = soup.find("input").get("value")
    URL = base64.b64decode(encodedUrl).decode('utf-8')

    return URL
