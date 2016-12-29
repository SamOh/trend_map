import sys
from flask import Flask, redirect, render_template, request, flash, url_for
import tweet_helper

app = Flask(__name__)
app.secret_key = 'something'


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":

        hashtag = request.form.get("hashtag")
        start_date = request.form.get("start_date")
        end_date = request.form.get("end_date")
        number_of_tweets = request.form.get("number_of_tweets")

        if hashtag == "":
            flash('Please fill out trend field')
            return redirect(url_for("search"))

        if start_date == "":
            flash('Please fill out start date field')
            return redirect(url_for("search"))

        if end_date == "":
            flash('Please fill out end date field')
            return redirect(url_for("search"))

        if number_of_tweets is None:
            flash('Please fill out number of tweets field')
            return redirect(url_for("search"))

        # Make sure hashtag includes the hashtag
        if hashtag[0] != "#":
            flash('hashtag must begin with a #')
            return redirect(url_for("search"))

        # Make sure start_date and end_date are in 2016-03-06 format
        if start_date[4] != "-" or start_date[7] != "-":
            flash('Start_date must be of form 2016-03-06')
            return redirect(url_for("search"))

        if end_date[4] != "-" or end_date[7] != "-":
            flash('end_date must be of form 2016-03-06')
            return redirect(url_for("search"))

        # Make sure user doesn't try to query greater than 999 tweets
        if int(number_of_tweets) > 1000 or int(number_of_tweets) < 1:
            flash('Number of tweets must be between 1 and 1000')
            return redirect(url_for("search"))

        user_info = tweet_helper.get_user_info_search(hashtag, start_date, end_date,
                                                      number_of_tweets)

        i = 0
        geo = []
        for tweet in user_info:
            if geo[i] != "":
                geo[i] = tweet.geo
                i += 1
            else:
                i += 1

        return render_template("map.html", geo=geo)

    else:
        return render_template("search.html")


@app.route("/map", methods=["GET", "POST"])
def map():
    return render_template("map.html")


@app.route("/first", methods=["GET", "POST"])
def first():
    if request.method == "POST":

        hashtag = request.form.get("hashtag")
        number_of_tweets = request.form.get("number_of_tweets")

        if hashtag == "":
            flash('Please provide screen name')
            return redirect(url_for("first"))

        if number_of_tweets is None:
            flash('Please provide integer between 1 and 1000')
            return redirect(url_for("first"))

        if hashtag[0] != '#':
            flash('Hashtag must begin with #')
            return redirect(url_for("first"))

        # Make sure user doesn't try to query greater than 999 tweets
        if int(number_of_tweets) > 1000 or int(number_of_tweets) < 1:
            flash('Number of tweets must be between 1 and 1000')
            return redirect(url_for("first"))

        user_info = tweet_helper.get_user_info_first(hashtag, number_of_tweets)

        i = 0
        text = []
        for tweet in user_info:
            text[i] = (tweet.username, tweet.text)
            i += 1

        return render_template("first.html", text=text, number=number_of_tweets)

    else:
        return render_template("first.html")


@app.route("/favorites", methods=["GET", "POST"])
def favorites():

    if request.method == "POST":

        screen_name = request.form.get("screen_name")
        start_date = request.form.get("start_date")
        end_date = request.form.get("end_date")

        if screen_name == "":
            flash('Please provide screen name')
            return redirect(url_for("favorites"))

        if screen_name[0] == '@':
            flash('Please dont include @ in user handle')
            return redirect(url_for("favorites"))

        if start_date == "":
            flash('Please fill out start date field')
            return redirect(url_for("favorites"))

        if end_date == "":
            flash('Please fill out end date field')
            return redirect(url_for("favorites"))

        # Make sure start_date and end_date are in 2016-03-06 format
        if start_date[4] != "-" or start_date[7] != "-":
            flash('Start_date must be of form 2016-03-06')
            return redirect(url_for("favorites"))

        if end_date[4] != "-" or end_date[7] != "-":
            flash('end_date must be of form 2016-03-06')
            return redirect(url_for("favorites"))

        user_info = tweet_helper.get_user_info_favorites(screen_name, start_date, end_date)

        number_of_favorites = 0
        number_of_tweets = 0
        for tweet in user_info:
            number_of_favorites += tweet.favorites
            number_of_tweets += 1

        average_num_of_favorites = number_of_favorites / number_of_tweets

        return render_template("favorites.html", average=average_num_of_favorites,
                               handle=screen_name)

    else:
        return render_template("favorites.html")
