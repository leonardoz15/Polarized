import re
import json
import tweepy
from tweepy import OAuthHandler
from twitter import TwitterClient
from train import TrainingML
from sentiment import PoliticalClassification
import matplotlib.pyplot as plt

api = TwitterClient()
trained_model = TrainingML()

def main():
    print("Welcome to my Comp :)\n")
    user = input("Twitter user to examine: \n")
    # creating object of TwitterClient Class
    # checking if user exists
    user_id = api.search_for_user(screen_name = user)
    # calling function to get tweets
    tweets = api.get_user_tweets(user_id = user_id, count = 200)

    model_choice = input("Which model suits you?\n0 = Naive Bayes\t1 = Linear SVM\n")
    print("Collecting and labeling tweets...\n")

    # appending user data to model for labeling
    for tweet in tweets:
        trained_model.predict_and_label(tweet, model_choice)
    # set of only tweets marked political
    political_tweets = [tweet for tweet in tweets if tweet['label'] == 'POLIT']

    for tweet in political_tweets:
        print(tweet['text'],"::\n")

if __name__ == '__main__':
    # calls main function
    main()
