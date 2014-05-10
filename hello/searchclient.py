import json
import time
#import lxml
from collections import namedtuple


#Global selections for payloads
api_key = ''
tags = list()

#def formatSearch(requests, title):
#    urlFormatSearch = 'http://api...' + title
#    time.sleep(0.6)
#    r = requests.get( urlFormatSearch, params = payload)
#    json_obj = r.json()
#    searchResults = list()
#    formatTypes = set()
#    titles = json_obj.get('titles')

#   for item in titles:
#        keyString = item['format'].get('id')
