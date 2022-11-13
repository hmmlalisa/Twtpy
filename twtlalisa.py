import pip

import tweepy
import random
from time import sleep

from io import BytesIO
from PIL import Image

def whats_my_name():
    client = tweepy.Client('AAAAAAAAAAAAAAAAAAAAAJnAdAEAAAAAHVd9CB7e6JV4gBwvRVTAL6q%2FoBM%3Dn38W7PlAsqLxlMtQf0IxyfuBAC8LVgOMk09IVT8xbAjZU5silB')
    auth = tweepy.OAuthHandler("3ZjLcRaA8e0sP7SF7UJEwKQQ5", "AYwCT07CnoaCfC7A7r2jpgUi7yIqP4IKqCTBj432BpTV0H3hMb")
    auth.secure = True
    consumer_key = "3ZjLcRaA8e0sP7SF7UJEwKQQ5"
    consumer_secret = "AYwCT07CnoaCfC7A7r2jpgUi7yIqP4IKqCTBj432BpTV0H3hMb"
    access_token = "1472165400951476224-2vbaqSoBbGv07AJFamSa3x1rwZXGV2"
    access_token_secret = "9zK65hLBEKWavIp1myw8Q8OeHoHRkPbAYpwqfp53Wadh0"

# Authentication with Twitter
    auth.set_access_token(access_token,     access_token_secret)
    api = tweepy.API(auth)
    
    #1 post a twt
    #2 reply
    #3 post a pic
    #4 quote a twt
    
    n = 3 #change here <<<<
    
# >>>>> post a twt <<<<<<

    if n == 1:
        api.update_status("""
Test
""")
        print("Successfully replied :)")
        
# >>>>> reply to a twt <<<<<<

    if n == 2:
    
        reply = "https://twitter.com/yvlalalisa/status/1577516128892760064?s=46&t=zAJHECply-rE_7Baazebtw"
        replx = reply[reply.find("status/")+7:reply.find("?")]
        message = ("""
Test
""")
    
        api.update_status(status=message, in_reply_to_status_id=replx, auto_populate_reply_metadata=True)
        print("Successfully replied :)")
        
# >>>>> post a pic/vid <<<<<<
        
    if n == 3:
        
        media =    api.media_upload(filename="a.PNG")

        message = ("""
Test
""")

        tweet = api.update_status(status=message, media_ids= 
    [media.media_id_string])
        
        print("Successfully replied :)")
        
# >>>>> quote a twt <<<<<<
    
    if n == 4:
        # Get the tweet you want to quote
        
        tweet_to_quote_url="https://twitter.com/lilieshome_/status/1568251145520558080?s=46&t=478yzomGcugKh5Q_F5xihw"
    
        #Quote it in a new status
        
        api.update_status("""
Test
""", attachment_url=tweet_to_quote_url)
        print("Successfully replied :)")

# Done


whats_my_name()
#chillin_like_a_villain()
