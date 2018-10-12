# Tweets_Analysis
Analysis of tweets text. Gives the sentiment analysis of all the tweets. The data file is included. Used NLTK and Python 3.

• Loding the data
• Processing and cleaning the data using punctuation, NLTK Stop words etc. Removing all the hashtags, alphatags, special    symbols etc.
• Computing the Sentiment Analysis of all the tweets.

I used NLTK to compute the Sentiment Analysis but it can also be done using the TextBlob library (python)

Code for textblob function is given below:

from textblob import TextBlob

def textblob_sentiment(arg1):  #arg1 can be any reviews, tweets and similar. Make sure to clean the data first.

    sentiment_textblob = TextBlob(reviews)

    return(sentiment_textblob.sentiment.polarity)
