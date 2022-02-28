from telnetlib import STATUS
import tweepy
import time  

auth = tweepy.OAuthHandler("qViOysKXR3lTFEMwBdlEUKVFS","6KsTNhw89ioLUYgExg82KpDGo2b015zOHwEGAUsCcf1x0YwEVq")
auth.set_access_token("1471941803519664137-nYHuxKPfdodiovYLR1Q9OloJZjAUqn","2qofxnh4XghqqY4RenW7ofBH0OaRRxrqIRQP4z4JHdiuL")

api = tweepy.API(auth)
tweet = "@InsertFriend'sUser Hi!"

api.update_status(status=(tweet))

#MUST UPDATE FOR OTHER VERSIONS OF TWITTER API!!!