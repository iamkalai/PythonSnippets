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
    with open(filename, "rt") as file:
        text = file.read()
    return text


# write a line to file
def writetofile(filename,text):
    with open(filename, "wt") as file:
        file.write(text)


# tweet and save the id back to file
def tweetandsaveid(filename, message):
    tweet_id_to_reply = readfromfile(filename)
    tweet = replymessage(message, tweet_id_to_reply)
    writetofile(filename, str(tweet.id))


# reply to a tweet
def replymessage(message, tweet_id):
    # add your Twitter app details here
    consumer_key = ""
    consumer_secret = ""
    access_key = ""
    access_secret = ""

    # sets up the authentication
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)

    # post the tweet and delete the image from disk
    api = tweepy.API(auth)
    return api.update_status(message, tweet_id)


tweet_id_file = "" # add the file path to be used for storing tweet id
counter_file = "" # add the file path to be used for storing day counter
message = "Day "+incrementdayscounter(counter_file)+" without pants."
tweetandsaveid(tweet_id_file,message)

