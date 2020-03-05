import re
import json
import tweepy
from tweepy import OAuthHandler
from twitter import TwitterClient
from train import TrainingML
from sentiment import PoliticalClassification

api = twitter.TwitterClient()

print("Welcome to my Comp :)\n")
user = input("Twitter user to examine: \t")
# creating object of TwitterClient Class
# checking if user exists
user_id = api.search_for_user(screen_name = user, count = 1)
# calling function to get tweets
tweets = api.get_user_tweets(user_id = user, count = 200)

# picking positive tweets from tweets
ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
# percentage of positive tweets
print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets)))
# picking negative tweets from tweets
ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
# percentage of negative tweets
print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets)))
# percentage of neutral tweets
print("Neutral tweets percentage: {} %".format(100*(len(tweets) - len(ntweets) - len(ptweets))/len(tweets)))

# printing first 5 positive tweets
print("\n\nPositive tweets:")
for tweet in ptweets[:10]:
	print(tweet['text'].encode("utf-8"))

# printing first 5 negative tweets
print("\n\nNegative tweets:")
for tweet in ntweets[:10]:
	print(tweet['text'].encode("utf-8"))
