from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search", methods=["GET", "POST"])
def search():
    # if request.method == "POST":

    return render_template("search.html")


@app.route("/first", methods=["GET", "POST"])
def first():
    return render_template("first.html")
