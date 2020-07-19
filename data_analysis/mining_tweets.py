import tweepy as tw
import pandas as pd
import csv


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
        self.tweet_count = 100
        self.search_words = self.search_term
        self.date_since = "2020-01-01"
        self.retweetfilter()
        self.tweetsearch()
        self.tweetarray()
        self.savetweets()

    def retweetfilter(self):
        # Filter out retweets
        return "#" + self.search_words + " -filter:retweets"

    def tweetsearch(self):
        # Search for tweets
        return tw.Cursor(self.api.search,
                         q=self.retweetfilter(),
                         lang="en",
                         since=self.date_since).items(self.tweet_count)

    def printtweet(self):
        # Method to take the search word then print out tweets
        for tweet in self.tweetsearch():
            print(tweet.text, sep='\n')

    def tweetarray(self):
        # Method to store tweets as a data frame
        return pd.DataFrame(data=self.tweetsearch())

    def savetweets(self):
        tweet_csv = pd.DataFrame(data=self.tweetsearch())
        return tweet_csv.to_csv(f"{self.search_words}.csv", encoding="utf-8")


if __name__ == "__main__":
    test = Exploration()
