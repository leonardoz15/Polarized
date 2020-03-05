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
