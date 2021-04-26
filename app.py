from tweet_builder import TweetBuilder

def handler(event, context):
  return TweetBuilder().post_tweet()

print(handler({}, 0))
