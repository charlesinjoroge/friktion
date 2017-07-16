from utils import is_ascii

import twitter

MAX_NUM_SEARCH_RESULTS = 20

def search_demo(api):
    results = api.GetSearch(term='politics', count=MAX_NUM_SEARCH_RESULTS)
    results = filter(lambda x: is_ascii(x.text) and is_ascii(x.user.name), results)
    
    print 'Twitter search results for politics...\n'
    for res in results:
        print 'This {0}tweet was written by {1}'.format(
            'possibly sensitive ' if res.possibly_sensitive else '', res.user.name)
        print 'It contains the following (expanded out) urls ->'
        for url in res.urls:
            print '\t' + url.expanded_url
        print 'The tweet itself is ->\n\t{0}'.format(res.text)
        print ''
    
