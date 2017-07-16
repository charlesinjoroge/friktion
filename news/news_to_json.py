import feedparser
import json
from utils import is_ascii


MAX_NUM_ENTRIES_PER_FEED = 300

# Could have a database table with these in them and read from that
# These are not all: http://www.cnn.com/services/rss/
cnn_feeds = [
    'http://rss.cnn.com/rss/cnn_topstories.rss',
    'http://rss.cnn.com/rss/cnn_world.rss',
    'http://rss.cnn.com/rss/cnn_us.rss',
    'http://rss.cnn.com/rss/money_latest.rss',
    'http://rss.cnn.com/rss/cnn_allpolitics.rss',
    'http://rss.cnn.com/rss/cnn_tech.rss',
    'http://rss.cnn.com/rss/cnn_latest.rss'
]

fox_feeds = [
    'http://feeds.foxnews.com/foxnews/latest',
    'http://feeds.foxnews.com/foxnews/national',
    'http://feeds.foxnews.com/foxnews/world',
    'http://feeds.foxnews.com/foxnews/politics',
    'http://feeds.foxnews.com/foxnews/scitech'
]

black_feeds = [
    'http://www.blackenterprise.com/feed/rss/',
    'http://www.blackenterprise.com/category/money/feed',
    'http://www.blackenterprise.com/category/technology/feed',
    'http://www.blackenterprise.com/category/news/feed',
    'http://www.blackamericaweb.com/rss/BAW/rss.xml',
    'http://www.blackprwire.com/rss/rss_all.php'
]

all_feeds = cnn_feeds + fox_feeds + black_feeds

arts = []
def main():
    global arts
    
    print 'News Feeds Demo'
    print '---------------'

    for feed in all_feeds:
        feed = feedparser.parse(feed)
        if not is_ascii(feed['feed']['title']):
            continue

        if feed['feed']['title'].lower().find('black') == -1:
            feed['entries'] = filter(lambda x: x['title'].lower().find('black') > -1, feed['entries'])
        feed['entries'] = filter(lambda x: is_ascii(x['title']), feed['entries'])
        size = min(MAX_NUM_ENTRIES_PER_FEED, len(feed['entries']))
        
        print '{0} has {1} entries'.format(feed['feed']['title'], len(feed['entries']))
        for entry in feed['entries'][:size]:
            arts += [{'title': entry['title'], 'link': entry['link']}]
    
    file = open('news.json', 'w')
    file.write(json.dumps(arts, indent=2))
main()

