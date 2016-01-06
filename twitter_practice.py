from twitter import *

from tokens import * 

t = Twitter(auth=OAuth(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET, TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET))


pythonTweets = t.search.tweets(q = "#python") 
print(pythonTweets)

pythonStatuses = t.statuses.user_timeline(screen_name="montypython", count=5)
print(pythonStatuses)

