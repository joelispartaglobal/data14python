import os
import tweepy as tw
import pandas as pd

class Exploration:
    def __init__(self):
        # Consumer and access keys from Twitter API
        self._consumer_key = 'wNYsBGLMFBs1v42NM7tMCn6jr'
        self._consumer_secret = 'EL5colsuyNkfNPLdzotPxL6idpNvEv43CeV61cZx6out2QtFde'
        self._access_token = '403403657-bGrDHSzLdwC8K66ooli52663xbhvOJMTbKBfs71h'
        self._access_token_secret = '0QzDmavOXLPqZtVzsZSNnrfba7vr1oQpIOe9xZt4PwNfd'
        self.auth = tw.OAuthHandler(self._consumer_key, self._consumer_secret)
        self.auth.set_access_token(self._access_token, self._access_token_secret)
        self.api = tw.API(self.auth, wait_on_rate_limit=True)
        self.search_term = input("Please input your search term: \n")
        self.tweet_count = int(input("Please input how many tweets you want to see: \n"))
        self.search_words = self.search_term
        self.date_since = "2018-11-16"

    def retweetfilter(self):
        # Filter out retweets
        return self.search_words + " -filter:retweets"

    def printtweet(self):
        # Method to take the search word then print out tweets
        tweets = tw.Cursor(self.api.search,
                           q=self.retweetfilter(),
                           lang="en",
                           since=self.date_since).items(self.tweet_count)
        for tweet in tweets:
            print(tweet.text, sep='\n')


test = Exploration()
print(test.printtweet())

# Collect a list of tweets
# tweet_collection = [tweet.text for tweet in tweets]
# print(tweet_collection)
#
# Use -filter:retweets to filter out retweets
# new_search = search_words + " -filter:retweets"

# tweets = tw.Cursor(api.search,
#                        q=new_search,
#                        lang="en",
#                        since=date_since).items(5)
#
# for tweet in tweets:
#     print(tweet.text)
#
# # Who's tweeting about cats?
#
# tweets = tw.Cursor(api.search,
#                            q=new_search,
#                            lang="en",
#                            since=date_since).items(5)
#
# users_locs = [[tweet.user.screen_name, tweet.user.location] for tweet in tweets]
# # print(users_locs)
#
# # Store users_locs as a dataframe using pandas
# tweet_text = pd.DataFrame(data=users_locs,
#                     columns=['user', "location"])
# print(tweet_text)
