from trending import trending_demo
from politics_search import search_demo

import twitter

NUM_STARS = 50

def print_with_emphasis(s):
    num_stars_left = NUM_STARS - len(s) - 2
    num_stars_beg = num_stars_left/2
    num_stars_end = num_stars_left - num_stars_beg

    print '*' * NUM_STARS
    print '*' * num_stars_beg, s, '*' * num_stars_end
    print '*' * NUM_STARS

def main():
    api = twitter.Api(consumer_key='EXaM6IAusM3ZZwiL4tGnEuiH5',
                      consumer_secret='ZiAiVOOPBIqchkmR9peJODhdE7eUwIILctYrUZd29fp9rLNJkd',
                      access_token_key='886305095498911744-hD57g0GKEeY8A6gjHzWXfXmJlcVj9vW',
                      access_token_secret='r55evis3xY7kRLMsaDZe5OXkIIJsypGbbSz9H5pQfzZjS')

    print_with_emphasis('trending demo')
    trending_demo(api)
    print_with_emphasis('search demo')
    search_demo(api)

main()
