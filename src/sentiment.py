import re
import json
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob

class PoliticalClassification(object):
	'''
	Class to handle sentiment and political classification
	'''
	def __init__(self):
		'''
		Class constructor or initialization method.
		'''


	def get_tweet_sentiment(self, tweet):
		'''
		Utility function to classify sentiment of passed tweet
		using textblob's sentiment method
		'''
		# create TextBlob object of passed tweet text
		analysis = TextBlob(self.clean_tweet(tweet))
		# set sentiment
		if analysis.sentiment.polarity > 0:
			return 'positive'
		elif analysis.sentiment.polarity == 0:
			return 'neutral'
		else:
			return 'negative'

	def classify_user(self,tweets):
		'''
		Classify user based on each tweet ratio -1 to 1
		'''

# # picking positive tweets from tweets
# ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
# # percentage of positive tweets
# print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets)))
# # picking negative tweets from tweets
# ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
# # percentage of negative tweets
# print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets)))
# # percentage of neutral tweets
# print("Neutral tweets percentage: {} %".format(100*(len(tweets) - len(ntweets) - len(ptweets))/len(tweets)))
#
# # printing first 5 positive tweets
# print("\n\nPositive tweets:")
# for tweet in ptweets[:10]:
# 	print(tweet['text'].encode("utf-8"))
#
# # printing first 5 negative tweets
# print("\n\nNegative tweets:")
# for tweet in ntweets[:10]:
# 	print(tweet['text'].encode("utf-8"))
