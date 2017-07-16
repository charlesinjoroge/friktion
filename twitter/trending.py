import sys, os
# Magic to add friktion to the set of paths search by Python
# Alternatively, update PYTHONPATH environment variable
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../")

from utils import is_ascii
from database.db import DBQuestionEntry as DBEntry

import twitter

NUM_TRENDING_TOPICS = 10

def to_db(trend):
    return DBEntry(topic=trend.name)

def trending_demo(api):
    # Gets worldwide trending topics. We can also specify a region (like USA or California or SF)
    trends = filter(lambda t: is_ascii(t.name), api.GetTrendsCurrent())
    
    print 'Trending topics'
    print '---------------'

    for trend in trends[:NUM_TRENDING_TOPICS]:
        print '{0} ->\n\tquery = {1}\n\turl = {2}\n\t# tweets = {3}\n'.format(
            trend.name, trend.query, trend.url, trend.tweet_volume)

    print "Now let's convert one of these things into a database entry"
    print "We have, for example"

    trend = trends[0]
    print '{0} ->\n\tquery = {1}\n\turl = {2}\n\t# tweets = {3}'.format(
            trend.name, trend.query, trend.url, trend.tweet_volume)
    print "As a database entry, this is"
    trend = to_db(trend)
    print trend
