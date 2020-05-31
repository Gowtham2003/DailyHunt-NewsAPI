# Coded By Gowtham on 30/05/2020
# Coded Using Vim Text Editor
from NewsData import newsData
queryDict = {
    'science': 'sci',
    'technology': 'tech',
    'india': 'ind',
    'automobile': 'auto',
    'entertainment': 'ent',
    'sport': 'spt',
    'world': 'wrd',
    'lifestyle': 'life',
    'employment': 'emp',
    'religion': 'rel',
    'football': 'foot',
    'movies': 'mov'
}


def getNews(category, language):

    query = category.lower()
    languageQuery = language.lower()

    return newsData(queryDict[query], languageQuery)
