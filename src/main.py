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
sentiment = PoliticalClassification()

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
    # get classification for each tweet in
    for tweet in political_tweets:
        tweet['classification'] = sentiment.get_tweet_sentiment(tweet['text'])

    left = []
    right = []
    for tweet in political_tweets:
        if tweet['classification'] != 0:
            if tweet['classification'] == -1:
                left.append(tweet)
            else:
                right.append(tweet)

    pleft = 100*len(left)/len(political_tweets)
    pright = 100*len(right)/len(political_tweets)
    print("Percent left leaning tweets {} %".format(pleft))
    print("Percent right leaning tweets {} %".format(pright))

    cont = input("Would you like a detailed analysis? (y/n)\n")
    if cont == 'y':
        print("Classification report for chose model:\n")
        if model_choice == 0:
            trained_model.get_classification_report_NB()
        else:
            trained_model.get_classification_report_SVM()
        if len(right) != 0:
            print("Right leaning tweets:\n")
            print(right['text'])
        elif len(left) != 0:
            print("Left leaning tweets:\n")
            print(left['text'])

    else:
        print("Have a nice day :)")


if __name__ == '__main__':
    # calls main function
    main()
