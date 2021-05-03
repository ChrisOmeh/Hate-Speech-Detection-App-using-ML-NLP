# import required libraries
from flask import *
import pandas as pd
import tweepy
import time


pd.set_option('display.max_colwidth', 1000)

# api key
api_key = "Mi1NZFqxZdsMKQzqsqlpa02Cr"
# api secret key
api_secret_key = "M3OU0kH3nbSeashz3tmpjrskgUYBfig3dZ84JQ1exKllGtYbL1"
# access token
access_token = "1386974524235829253-MQvIjjDdFP16X4SB2lQa6HIQFLRhgk"
# access token secret
access_token_secret = "G2JzgZCIUP8d1w1s3kGmHkgoSMuZzSiN1JOPr1towjhVp"

# authorize the API Key
authentication = tweepy.OAuthHandler(api_key, api_secret_key)

# authorization to user's access token and access token secret
authentication.set_access_token(access_token, access_token_secret)

# call the api
api = tweepy.API(authentication, wait_on_rate_limit=True)


def fetch_tweets(text_query):
    # list to store tweets
    tweets_list = []
    # no of tweets
    count = 100
    try:
        # Pulling individual tweets from query
        for tweet in api.search(q=text_query, count=count):
            print(tweet.text)
            # Adding to list that contains all tweets
            tweets_list.append({'created_at': tweet.created_at,
                                'tweet_id': tweet.id,
                                'tweet_text': tweet.text})
        return pd.DataFrame.from_dict(tweets_list)

    except BaseException as e:
        print('failed on_status,', str(e))
        time.sleep(3)
