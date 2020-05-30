from NewsData import newsData
queryDict = {
        'science':'sci',
        'technology':'tech',
        'india':'ind',
        'automobile':'auto',
        'entertainment':'ent',
        'sport':'spt',
        'world':'wrd',
        'lifestyle':'life',
        'employment':'emp',
        'religion':'rel',
        'football':'foot',
        'movies':'mov'
        }
def getNews(category):

    query = category.lower()

    return newsData(queryDict[query])


