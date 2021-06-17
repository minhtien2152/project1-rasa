import requests

def Searcher(keyword,limit): 
    url='https://immense-garden-76522.herokuapp.com/api/courses'
    json_data = requests.get(url,params={'keyword':f"{keyword}", "limit":limit}).json() 
    return json_data