import os
import getoldtweets

"""Returns a list of key value pairs (user_location, time_tweeted)"""


def get_user_info(hashtag, start_date, end_date, number_of_tweets):

    # Get tweets based on hashtag
    # https://github.com/Jefferson-Henrique/GetOldTweets-python
    tweetCriteria = getoldtweets.got.manager.TweetCriteria().setQuerySearch(hashtag).setSince(
        start_date).setUntil(end_date).setMaxTweets(number_of_tweets)
    list_of_tweets = getoldtweets.got.manager.TweetManager.getTweets(tweetCriteria)

    return list_of_tweets
