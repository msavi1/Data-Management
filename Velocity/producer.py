# -*- coding: utf-8 -*-
"""
Librerie
"""

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from kafka import KafkaProducer
import tweepy
import time
import json

"""Chiavi di Twitter"""

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

producer = KafkaProducer(bootstrap_servers=["localhost:9092"], 
                         value_serializer=lambda v: json.dumps(v, default=str).encode("utf-8"))

topic_name = 'LCDP'

class listener(StreamListener):

     def on_status(self, status):
            tweet = {
                'user_id': status.id, 
                'created_at': status.created_at, 
                'screen_name': status.user.screen_name, 
                'text': status.text, 
                'source': status.source,
                'lang': status.lang,
                'hashtags': []
    } 
            if status.entities.get('hashtags') is not None:
                hashtags = status.entities.get('hashtags')
                tweet['hashtags'] = [h.get('text') for h in hashtags] 
                producer.send(topic=topic_name, value=tweet) 
                
                def on_error(self, status): 
                    print('Got an error with status code: ' + str(status_code)) 
                    return True 
                
if __name__ == '__main__': 
    auth = OAuthHandler(consumer_key, consumer_secret) 
    auth.set_access_token(access_token, access_secret) 
    api = tweepy.API(auth) 
    stream = listener 
    stream = Stream(auth = api.auth, listener=stream()) 
    stream.filter(track=['lacasadepapel'], languages=["it", "en", "es"])
