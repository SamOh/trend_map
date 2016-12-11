import os
from getoldtweets import got3
from bs4 import BeautifulSoup

"""Returns a list of key value pairs (user_location, time_tweeted)"""


def get_user_info(hashtag, start_date, end_date, number_of_tweets=150):

    # Get tweets based on hashtag
    # https://github.com/Jefferson-Henrique/GetOldTweets-python
    tweetCriteria = got3.manager.TweetCriteria().setQuerySearch(hashtag).setSince(
        start_date).setUntil(end_date).setMaxTweets(number_of_tweets)
    list_of_tweets = got3.manager.TweetManager.getTweets(tweetCriteria)

    return list_of_tweets


test1 = get_user_info('#feelthebern', '2016-08-01', '2016-08-20', 10)
for tweet in test1:
    print(tweet.text)
    print(tweet.geo)


# Relic of past tests
# html = BeautifulSoup(str(test1[0].tweetPQ), "lxml")
# rawhtml = BeautifulSoup(str(test1[0].rawhtml), "lxml")
# tweets = BeautifulSoup(str(test1[0].tweets), "lxml")
# alljson = BeautifulSoup(str(test1[0].alljson), "lxml")
# location = test1[0].geo
# print(location)
