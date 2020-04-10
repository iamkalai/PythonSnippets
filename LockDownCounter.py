import os
import tweepy


# read and increment the days counter
def incrementdayscounter(filename):
    days = readfromfile(filename)
    days = int(days) + 1
    writetofile(filename,str(days))
    return str(days)


# read a line from file
def readfromfile(filename):
    text = ""
    with open(filename, "r") as file:
        text = file.readline()
        file.close()
    return text


# write a line to file
def writetofile(filename,text):
    with open(filename, "w") as file:
        file.write(text)
        file.close()


# reply to a tweet
def replyMessage(message, tweet_id):
    # add your Twitter app details here
    CONSUMER_KEY = "add here"
    CONSUMER_SECRET = "add here"
    ACCESS_KEY = "add here"
    ACCESS_SECRET = "add here"

    # sets up the authentication
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

    # post the tweet and delete the image from disk
    api = tweepy.API(auth)
    return (api.update_status(message, tweet_id))



tweet_id_to_reply = readfromfile("tweetid.txt")
days = incrementdayscounter("counter.txt")
message = "Day "+days+" without pants."
tweet = replyMessage(message,tweet_id_to_reply)
writetofile("tweetid.txt",str(tweet.id))
