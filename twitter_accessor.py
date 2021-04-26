from secrets import *
import tweepy

class TwitterAccessor:
  def __init__(self):
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    self.api = tweepy.API(auth)

  def read_last_tweet(self):
    timeline = self.api.home_timeline(count=1, exclude_replies=True, tweet_mode='extended')
    return timeline[0].full_text
