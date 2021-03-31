import tweepy
from textblob import TextBlob
import twitterapi


"""
# Rename sample_twitterapi.py to twitterapi.py
# Add your api keys in sample_twitterapi.py

"""

auth = tweepy.OAuthHandler(twitterapi.consumer_key, twitterapi.consumer_secret)
auth.set_access_token(twitterapi.access_token, twitterapi.access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('#Covid19')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis)