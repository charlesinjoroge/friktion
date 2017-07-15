import twitter
# Maybe unneccesary import but just in case...
import json

NUM_TRENDING_TOPICS = 20

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

def main():
    api = twitter.Api(consumer_key='EXaM6IAusM3ZZwiL4tGnEuiH5',
                      consumer_secret='ZiAiVOOPBIqchkmR9peJODhdE7eUwIILctYrUZd29fp9rLNJkd',
                      access_token_key='886305095498911744-hD57g0GKEeY8A6gjHzWXfXmJlcVj9vW',
                      access_token_secret='r55evis3xY7kRLMsaDZe5OXkIIJsypGbbSz9H5pQfzZjS')
   
    # Gets worldwide trending topics. We can also specify a region (like USA or California or SF)
    trends = filter(lambda t: is_ascii(t.name), api.GetTrendsCurrent())
    
    print 'Trending topics'
    print '---------------'

    for trend in trends[:NUM_TRENDING_TOPICS]:
        print '{0} ->\n\tquery = {1}\n\turl = {2}\n\t# tweets = {3}\n'.format(
            trend.name, trend.query, trend.url, trend.tweet_volume)

main()
