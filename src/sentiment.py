import nltk
from textblob import TextBlob
import pandas as pd
from operator import itemgetter

class PoliticalClassification(object):
		'''
		Class to handle sentiment and political classification
		'''
		def __init__(self):
				'''
				Class constructor, initializes dictionary for political classification
				'''

				rep_tweets = pd.read_csv("../data/ExtractedTweets2.csv", header='infer')
				rep_tweets.columns = ['Party', 'Handle', 'Tweet']
				representatives = rep_tweets.drop(columns='Tweet')
				representatives = representatives.drop_duplicates()

				# dictionary to store politcians and their party
				self.politicians = representatives.to_dict('records')
				# for entry in self.politicians:
				# 	if "SenWarren" in entry['Handle']:
				# 		print(entry['Party'])

		def get_nouns(self, blob):
				'''
				Utility function to classify sentiment of passed tweet
				using textblob's sentiment method
				'''

				return blob.noun_phrases

		def get_tweet_sentiment(self, tweet):
				'''
				Utility function to classify sentiment of passed tweet
				using textblob's sentiment method
				'''

				# create TextBlob object of passed tweet text
				blob = TextBlob(tweet)
				# attempt spelling correction
				blob.correct()
				# float to hold polarity of tweet
				polarity = blob.polarity

				noun_list = self.get_nouns(blob)

				ratio = self.classify_tweet(polarity, noun_list)

				return ratio

		def classify_tweet(self, polarity, nouns):
				'''
				Classify user based on each tweet ratio -1 to 1
				'''
				# -1 = left leaning, 0 = neutral, 1 = right leaning
				tweet_ratio = 0
				for noun in nouns:
					for entry in self.politicians:
						if noun in entry['Handle']:
							party = entry['Party']
							if polarity > 0 and party == 'Democrat':
								tweet_ratio = -1
								return tweet_ratio
							elif polarity > 0 and party == 'Republican':
								tweet_ratio = 1
								return tweet_ratio
							elif polarity < 0 and party == 'Democrat':
								tweet_ratio = 1
								return tweet_ratio
							elif polarity < 0 and party == 'Republican':
								tweet_ratio = -1
								return tweet_ratio
						else:
							return 0
