import os
import tweepy as tw
import pandas as pd

consumer_key = 'wNYsBGLMFBs1v42NM7tMCn6jr'
consumer_secret = 'EL5colsuyNkfNPLdzotPxL6idpNvEv43CeV61cZx6out2QtFde'
access_token = '403403657-bGrDHSzLdwC8K66ooli52663xbhvOJMTbKBfs71h'
access_token_secret = '0QzDmavOXLPqZtVzsZSNnrfba7vr1oQpIOe9xZt4PwNfd'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

# Define the search term and the date_since date as variables
search_words = "#cats"
date_since = "2018-11-16"


# Collect tweets
tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items(5)

# Iterate and print tweets
for tweet in tweets:
    print(tweet.text)

