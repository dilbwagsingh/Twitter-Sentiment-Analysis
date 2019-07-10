import tweepy
from textblob import TextBlob

consumer_key = 'vlQcinxCcBKCK4VD3gttj22iQ'
consumer_secret = 'SIOWCT55CV4UmUXHDZEHJs0NsEQQq0Mj6wVQGbSpEVrsnFokdb'

access_token = '1101309721-1a8niUIgHDLQg2wwtkoMd0t9CwPKLneERfx8YDV'
access_token_secret = 'Og4lL203iVxre73uQbTjRKbA8Lnheiiqy8K7RLgiEK9wU'

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
