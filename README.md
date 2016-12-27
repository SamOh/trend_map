# trend_map
Application that uses twitter API to show a map of where a trend originated, and how it has spread/progressed over time.

### Tech used
Part of the reason I wanted to do this was also to learn to use some new tech such as the tech below:
+ D3
+ Flask/python
+ Google Maps API
+

### Credits
Started out using the twitter API, but quickly realized the limitations on the number of tweets I could query (stops at about 1-2 weeks back),
so I had to find an alternative. Found code at https://github.com/Jefferson-Henrique/GetOldTweets-python that works around the limitations set
by twitter, however, the code as it was could not extract the lat/long attributes of a tweet
so I added code to find the geographical location the user was from.
