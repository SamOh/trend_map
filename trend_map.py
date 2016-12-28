import sys
from flask import Flask, redirect, render_template, request, url_for

import tweet_helper

app = Flask(__name__)


@app.route("/")
def index():
    if request.method == "POST":

        # make sure screen name is valid
        if request.form.get("screen_name") == "":
            return redirect(url_for("index"))

        # make sure hashtag is valid
        if request.form.get("hashtag") == "":
            return redirect(url_for("index"))

        # make sure start date is valid
        if request.form.get("start_date") == "":
            return redirect(url_for("index"))

        # make sure end date is valid
        if request.form.get("end_date") == "":
            return redirect(url_for("index"))

        # find number of tweets being asked for and search for it
        if request.form.get("number_of_tweets") == "":
            return redirect(url_for("index"))

        hashtag = request.form.get("hashtag")
        screen_name = request.form.get("screen_name")
        start_date = request.form.get("start_date")
        end_date = request.form.get("end_date")
        number_of_tweets = request.form.get("number_of_tweets")

        user_info = tweet_helper.get_user_info(hashtag, start_date, end_date, number_of_tweets)

        return render_template("search.html", )

    else:
        return render_template("index.html")


@app.route("/search", methods=["GET", "POST"])
def search():
    return render_template("search.html")


@app.route("/first", methods=["GET", "POST"])
def first():
    return render_template("first.html")
