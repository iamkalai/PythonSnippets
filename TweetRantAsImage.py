#This snippet will allow you to post a rant from devRant to Twitter as image

from urllib import request
import os
import tweepy

#add your Twitter app details here
CONSUMER_KEY ="add here"
CONSUMER_SECRET = "add here"
ACCESS_KEY = "add here"
ACCESS_SECRET = "add here"

#sets up the authentication
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

#reads the url as input from user
tempImage = "image.png"
imagePath = input("Enter Rant URL")
lastSlash = imagePath.rfind("/")
url = imagePath[:lastSlash+1]+tempImage

#reads the image from devRant rant and stores in system
request.urlretrieve(url,tempImage)
message = "#devrant"

#post the tweet and delete the image from disk
api = tweepy.API(auth)
api.update_with_media(tempImage,message)
os.remove(tempImage)
