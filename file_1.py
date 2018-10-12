import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
import re

def get_list(arg1, arg2, arg3):
    for i in range(0,len(arg1)):
        for j in range(0,len(arg1[i])):
            arg2.append(arg1[i][j][arg3])
    return arg2

def get_list_two(arg1, arg2, arg3,arg4):
    for i in range(0,len(arg1)):
        for j in range(0,len(arg1[i])):
            arg2.append(arg1[i][j][arg3][arg4])
    return arg2

def text_cleaning(arg1):
    stopwords = nltk.corpus.stopwords.words("english")
    text_list_clean = arg1[:]
    word_tokens = word_tokenize(str(text_list_clean))
    text_list_clean = [w for w in word_tokens if not w in stopwords]
    text_list_clean =[]
    for w in word_tokens:
        if w not in stopwords:
            text_list_clean.append(w)
    table = str.maketrans({key: None for key in string.punctuation})
    text_list_clean = str(text_list_clean).translate(table)
    table1 = str.maketrans({key: None for key in string.digits})
    text_list_clean=str(text_list_clean).translate(table1)
    tokens = nltk.tokenize.word_tokenize(text_list_clean)
    return tokens

#cwctweets looks like a json file, but is not
#read it in and use eval to convert each line to a dictionary
#then append it to a list
#there should be ten dictionaries in the list

tweet_dict = []
with open('cwctweets.txt','r') as inf:
    for line in inf:
        tweet_dict.append(eval(line))

#display all the tweets
print("Printing all the tweets: \n\n{}".format(tweet_dict))
print("\n\n")

#Check the length of d
print("length of d is: {}".format(len(tweet_dict)))
print("\n\n")

#Display the first element of d - check its length as well
print("The first element of d is: \n\n\n {}".format(tweet_dict[0]))
print("\n\n")
print("the length of the first element is: {}".format(len(tweet_dict[0])))
print("\n\n")

#Get all 'statuses' using key 'statuses'
statuses_list=[]
for i in tweet_dict:
    statuses_list.append(i['statuses'])
print("Printing the statuses: \n\n{}".format(statuses_list))
print("\n\n")

#use each status to get text - text is a key
text_list = []
get_list(statuses_list,text_list,'text')
print("Printing the text: \n\n{}".format(text_list))
print("\n\n")

#get the locations from where the tweets were sent, if available
location_list = []
get_list_two(statuses_list,location_list,'user','location')
location_list_ = filter(None,location_list)
print("Printing the locaitons: \n\n{}".format(list(location_list_)))
print("\n\n")

#Find the top 5 hashtags used in the tweets - hint look at 'entities'
#under each status; then look at 'hashtags' under 'entities'
hashtags_list = []
get_list_two(statuses_list,hashtags_list,'entities','hashtags')
hashtag_text_list = []
get_list(hashtags_list,hashtag_text_list,'text')
fdist = nltk.FreqDist(hashtag_text_list)
print("The top 5 Hashtags are: \n\n")
for word, frequency in fdist.most_common(5):
    print(u'{};{}'.format(word, frequency))

#Create a frequency plot of the top 25 words
#hint: use nltk.FreqDist
fdist_top_25 = nltk.FreqDist(text_cleaning(text_list))
fdist_top_25.plot(25, cumulative=False)

#Display the total sentiment score for each tweet
#output should be in the following format:
#Tweet#  User   Country      Sentiment Score
user_list = []
get_list_two(statuses_list,user_list,'user','name')
s = SentimentIntensityAnalyzer()
print("#Tweet#                      User            Country               Sentiment Score  ")
print("\n\n")
text_list_clean = text_cleaning(text_list)
for i in range(0,len(text_list)):
    print("{}                          {}                {}                    {}   ".format(text_list[i],user_list[i],location_list[i],s.polarity_scores(text_list_clean[i])))
