from telnetlib import STATUS
import tweepy
import time  

auth = tweepy.OAuthHandler("insert key1, insert key 2")
auth.set_access_token("insert other keys 1, and 2")

api = tweepy.API(auth)
tweet = "@InsertFriend'sUser Hi!"

api.update_status(status=(tweet))

#MUST UPDATE FOR OTHER VERSIONS OF TWITTER API!!!
