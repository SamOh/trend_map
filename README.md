# trend_map
Application that uses twitter API to show a map of where a trend originated, and how it has spread/progressed over time.

### Credits
Started out using the twitter API, but quickly realized the limitations on the number of tweets I could query (stops at about 1-2 weeks back),
so I had to find an alternative. Found code at https://github.com/Jefferson-Henrique/GetOldTweets-python that works around the limitations set
by twitter, however, the code as it was could not extract the lat/long attributes of a tweet
so I added code to find the geographical location the user was from.

### UPDATE
Unfortunately, despite spending a lot of time working on the onofficial API to query twitter and get
responses, as of ~1/03/16 twitter updated it's site and is no longer compatible with the code, so
I have to swtich back to the twitter API and work with the restrictions in place.
