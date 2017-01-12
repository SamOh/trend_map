import os
from settings import get_env_variable
import requests
from TwitterSearch import *
from twython import Twython
from twython.exceptions import TwythonAuthError



def get_user_info_search(hashtag, number_of_tweets=150):

    # Get tweets based on hashtag
    try:
        results = TwitterSearchOrder()
        results.set_keywords([hashtag])
        results.set_include_entities(False)

        # it's about time to create a TwitterSearch object with our secret tokens
        search = TwitterSearch(
            consumer_key = get_env_variable('BqFjugffuK0CKMXoXmrkmcTVK'),
            consumer_secret = get_env_variable('nOaTOkz1qGmDshOXJMSVo0qZBjFNYi8qRC8XqBYy0HXIFe89uv'),
            access_token = get_env_variable('790574704302129152-Opnh5Mb4bGjET8QqmSuxkrDoXSflbwn'),
            access_token_secret = get_env_variable('Jl5fU3gCcOWniVekuGgiXDjW3hf6joq61bhpVu3xNXoYi')
         )

        # get tweet information
        for tweet in search.search_tweets_iterable(results):
            print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )

    except TwitterSearchException as e: # take care of all those ugly errors if there are some
        print(e)

get_user_info_search('#something')

# def get_user_info_first(hashtag, number_of_tweets=150):

#     return list_of_tweets


def get_user_info_favorites(screen_name, start_date, end_date):

    from TwitterSearch import *

    try:
        user_serach = TwitterUserOrder('NeinQuarterly') # create a TwitterUserOrder

        # it's about time to create TwitterSearch object again
        search = TwitterSearch(
            consumer_key = 'aaabbb',
            consumer_secret = 'cccddd',
            access_token = '111222',
            access_token_secret = '333444'
        )

        # start asking Twitter about the timeline
        for tweet in ts.search_tweets_iterable(tuo):
            print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )

    except TwitterSearchException as e: # catch all those ugly errors
        print(e)

    # get screen_name's most recent tweets
    # try:
    #     twitter = Twython(settings.get_env_variable("API_KEY"),
    #                       settings.get_env_variable("API_SECRET"))
    #     tweets = GET https://api.twitter.com/1.1/search/tweets.json?q=%23freebandnames&since_id=24012619984051000&max_id=250126199840518145&result_type=mixed&count=4
    #     print
    #     # tweets = twitter.get_user_info_favorites(screen_name=screen_name, count=count)
    #     # return [html.unescape(tweet["text"].replace("\n", " ")) for tweet in tweets]
    # except TwythonAuthError:
    #     return None

    # return number_of_favorites





