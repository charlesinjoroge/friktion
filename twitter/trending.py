import twitter

def main():
    api = twitter.Api(consumer_key='EXaM6IAusM3ZZwiL4tGnEuiH5',
                      consumer_secret='ZiAiVOOPBIqchkmR9peJODhdE7eUwIILctYrUZd29fp9rLNJkd',
                      access_token_key='886305095498911744-hD57g0GKEeY8A6gjHzWXfXmJlcVj9vW',
                      access_token_secret='r55evis3xY7kRLMsaDZe5OXkIIJsypGbbSz9H5pQfzZjS')
    print 'credentials:', api.VerifyCredentials()

main()
