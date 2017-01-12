import os
from getoldtweets import got3
from bs4 import BeautifulSoup

"""Returns a list of key value pairs (user_location, time_tweeted)"""


def get_user_info_search(hashtag, start_date, end_date, number_of_tweets=150):

    # Get tweets based on hashtag
    tweetCriteria = got3.manager.TweetCriteria().setQuerySearch(hashtag).setSince(
        start_date).setUntil(end_date).setMaxTweets(number_of_tweets)
    list_of_tweets = got3.manager.TweetManager.getTweets(tweetCriteria)

    return list_of_tweets


def get_user_info_first(hashtag, number_of_tweets=150):

    tweetCriteria = got3.manager.TweetCriteria().setQuerySearch(hashtag).setMaxTweets(
        number_of_tweets).setSince('2006-03-21')
    list_of_tweets = got3.manager.TweetManager().getTweets(tweetCriteria)

    return list_of_tweets


def get_user_info_favorites(screen_name, start_date, end_date):

    tweetCriteria = got3.manager.TweetCriteria().setUsername(screen_name).setSince(
        start_date).setUntil(end_date).setMaxTweets(1)
    list_of_tweets = got3.manager.TweetManager().getTweets(tweetCriteria)

    return list_of_tweets


test1 = get_user_info_search('#harambe', '2016-07-01', '2016-10-30', 5)
print(test1)
for tweet in test1:
    print(tweet.text)
    print(tweet.geo)
    print(tweet.mentions)
    print(tweet.favorites)
    print(tweet.formatted_date)

# tweetCriteria = got3.manager.TweetCriteria().setUsername('chicagobulls').setMaxTweets(1)
# tweet = got3.manager.TweetManager.getTweets(tweetCriteria)

# print(tweet)

# test2 = get_user_info_favorites('chicagobulls', '2016-12-29', '2016-12-29')
# print(test2)
# for tweet in test2:
#     print(tweet.text)
#     print(tweet.favorites)
#     print('hello')

# Relic of past tests
# html = BeautifulSoup(str(test1[0].tweetPQ), "lxml")
# rawhtml = BeautifulSoup(str(test1[0].rawhtml), "lxml")
# tweets = BeautifulSoup(str(test1[0].tweets), "lxml")
# alljson = BeautifulSoup(str(test1[0].alljson), "lxml")
# location = test1[0].geo
# print(location)
