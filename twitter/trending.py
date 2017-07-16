from utils import is_ascii

import twitter

NUM_TRENDING_TOPICS = 20

def trending_demo(api):
    # Gets worldwide trending topics. We can also specify a region (like USA or California or SF)
    trends = filter(lambda t: is_ascii(t.name), api.GetTrendsCurrent())
    
    print 'Trending topics'
    print '---------------'

    for trend in trends[:NUM_TRENDING_TOPICS]:
        print '{0} ->\n\tquery = {1}\n\turl = {2}\n\t# tweets = {3}\n'.format(
            trend.name, trend.query, trend.url, trend.tweet_volume)
