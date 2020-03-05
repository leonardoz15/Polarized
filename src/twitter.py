import re
import json
import tweepy
from tweepy import OAuthHandler

class TwitterClient(object):
	'''
	Generic Twitter Class for API handling.
	'''
	def __init__(self):
		'''
		Class constructor or initialization method for authorization.
		'''
		# Twitter Dev Console credentials in client.json
		with open ("../secret/client.json") as f:
			client = json.load(f)
		# keys and tokens from the client.json
		consumer_key = client["consumer_key"]
		consumer_secret = client["consumer_key_secret"]
		access_token = client["access_token"]
		access_token_secret = client["access_token_secret"]


		# attempt authentication
		try:
			# create OAuthHandler object
			self.auth = OAuthHandler(consumer_key, consumer_secret)
			# set access token and secret
			self.auth.set_access_token(access_token, access_token_secret)
			# create tweepy API object to fetch tweets
			self.api = tweepy.API(self.auth)
		except:
			print("Error: Authentication Failed")

	def search_for_user(self, screen_name, count):
		'''
		Verifies that searched user exists
		'''
		# list to store user objects in
		users = []
		# search Twitter for specified screen_name
		user = self.api.search_users(q = screen_name, count = count)

		# Verifies query is successful
		if len(user) != 0:
			inspect_user = user[0]
			real_id = inspect_user.id
			print("Found user: ", inspect_user.screen_name)
			print("User id: ", real_id)
			return real_id
		else:
			print("No user with that name")

	def clean_tweet(self, tweet):
		'''
		Utility function to clean tweet text by removing links, special characters
		using simple regex statements.
		'''
		return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def get_user_tweets(self, user_id, count):
        '''
        Main function to fetch tweets from a user and parse them.
        '''
        # empty list to store parsed tweets
        tweets = []

        try:
            # call twitter api to fetch tweets
            fetched_tweets = self.api.user_timeline(user_id = user_id, count = count)

            # parsing tweets one by one
            for tweet in fetched_tweets:
                # empty dictionary to store required params of a tweet
                parsed_tweet = {}

                # saving text of tweet
                parsed_tweet['text'] = self.clean_tweet(tweet.text)

                # appending parsed tweet to tweets list
                if tweet.retweet_count > 0:
                    # if tweet has retweets, ensure that it is appended only once
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)

            # return parsed tweets
            return tweets

        except tweepy.TweepError as e:
            # print error (if any)
            print("Error : " + str(e))
