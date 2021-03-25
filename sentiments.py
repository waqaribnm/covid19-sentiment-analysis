import tweepy
from textblob import TextBlob
import twitterapi


"""
# Remove comments and add your api key.
# Also remove twitterapi import.
consumer_key = ''
consumer_secret = ''

access_token = ''
access_token_secret = ''
"""

auth = tweepy.OAuthHandler(twitterapi.consumer_key, twitterapi.consumer_secret)
auth.set_access_token(twitterapi.access_token, twitterapi.access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('#Covid19')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis)