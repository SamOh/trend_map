import os

from twython import Twython
from twython.exceptions import TwythonAuthError

from settings.py import API_KEY, API_SECRET

"""Returns a list of key value pairs (user_location, time_tweeted)"""


def get_user_info(hashtag, start_date, end_date):

    # Get tweets
    # https://github.com/ryanmcgrath/twython/blob/master/twython/endpoints.py
    try:
        twitter = Twython(API_KEY, API_SECRET)
        tweets = twitter.get_user_timeline(screen_name=screen_name, count=count)
        return [html.unescape(tweet["text"].replace("\n", " ")) for tweet in tweets]
    except TwythonAuthError:
        return None
