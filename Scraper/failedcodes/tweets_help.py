import os
import tweepy as tw
import pandas as pd

consumer_key= ''
consumer_secret= ''
access_token= ''
access_token_secret= ''




def main():
    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tw.API(auth, wait_on_rate_limit=True)

    for tweet in api.search_tweets(q="covid", lang="en"):
        print(tweet.text)


if __name__ == "__main__":
    main()
