import feedparser

MAX_NUM_ENTRIES_PER_FEED = 3

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

all_feeds = cnn_feeds + fox_feeds

def main():
    print 'News Feeds Demo'
    print '---------------'

    for feed in all_feeds:
        feed = feedparser.parse(feed)
        size = min(MAX_NUM_ENTRIES_PER_FEED, len(feed['entries']))
        
        print '{0} has {1} entries'.format(feed['feed']['title'], len(feed['entries']))
        print 'Here are the the first {0} of them ->'.format(size)
        for entry in feed['entries'][:size]:
            print '\t"{0}" found at\n\t\t{1}'.format(
                entry.get('title', '*unknown title*'), entry.get('link', '*unkown link*'))

main()
