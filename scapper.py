import tweepy
from textblob import TextBlob

consumer_key = ''
consumer_secret = ''

access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.search, q='NVidia -filter:retweets', rpp=100).items(50):
	# tweet.split('\'text\': ')
	# tweet[1].split('\'truncated\':')
	if tweet.lang == "en":	
		sauce = tweet.text.split('http')
		blob = TextBlob(sauce[0]) 
		print(sauce[0])
		sentiment = blob.sentiment.polarity
		if sentiment >=0:
			print("Positive")
		else:
			print("Negative")
