from tweepy import API
from tweepy import Cursor
from tweepy import OAuthHandler
from textblob import TextBlob

import re
import matplotlib.pyplot as plt
import twitter_credentials
import numpy as np 
import pandas as pd


accounts = ["AToddLegacy","STOMPOutBullyng","ActToChange","AntiBullyingPro","c_todd","NicoleMCrowther","Pattiagatston","MindofAndrew","AntiBullyingCen","StopBullyingGov","eSafetyOffice","UK_SIC"]
hashtags = ['cyberbullying', 'bullying', 'STOMPOutBullying', 'PinkShirtDay','ActToChange','StandUpToBullying', 'StopBullying','SaferInternetDay']
                                        
class TwitterClient():

    def __init__(self, twitter_user=None):
        self.auth = OAuthHandler(twitter_credentials.CONSUMER_KEY,twitter_credentials.CONSUMER_SECRET)
        self.auth.set_access_token(twitter_credentials.ACCESS_TOKEN,twitter_credentials.ACCESS_TOKEN_SECRET)
        self.twitter_client = API(self.auth)
        self.twitter_user = twitter_user

    def get_twitter_client_api(self):
        return self.twitter_client

class TweetAnalyzer():
    #Functionality for analyzing and categorizing content from tweets

    def contain_hashtags(self,tweet):
        flag = False
        for ht in tweet.entities['hashtags']:
            if(ht['text'].lower() in hashtags):
                flag = True
            # else:     #uncomment else block to print hashtags that are filtered out
                # print(ht['text'].lower())
        return flag

    def filter_tweets(self,tweets):
        filtered = []
        for tweet in tweets:
            r = self.contain_hashtags(tweet)
            if(r==True): filtered.append(tweet)
        return filtered

    def clean_tweet(self,tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def tweets_to_data_frame(self,tweets):
        df = pd.DataFrame(data=[tweet.full_text for tweet in tweets], columns=['tweets'])
        df['author']    = np.array([tweet.user._json['screen_name'] for tweet in tweets])
        df['retweets']  = np.array([tweet.retweet_count for tweet in tweets])
        df['likes']     = np.array([tweet.favorite_count for tweet in tweets])
        df['date']      = np.array([tweet.created_at for tweet in tweets])
        return df


if __name__ == "__main__":

    frames=[]
    twitter_client = TwitterClient()
    tweet_analyzer = TweetAnalyzer()

    hashtags = [x.lower() for x in hashtags]

    api = twitter_client.get_twitter_client_api()
    for screen_name in accounts:
        tweets = api.user_timeline(screen_name=screen_name,count=300, tweet_mode='extended')
        df = tweet_analyzer.tweets_to_data_frame( tweet_analyzer.filter_tweets(tweets) )
        frames.append(df)
        
    result = pd.concat(frames)

    print(result.head(300))
    result.to_csv('conclusions.csv', encoding='utf-8', index = False, header=True)

   
