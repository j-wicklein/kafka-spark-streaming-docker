from kafka import KafkaProducer
import time
import json
from datetime import datetime
import twitter_data
#from setup_logger import fetch_log 

producer = KafkaProducer(bootstrap_servers="kafka:9092")

twitterFetcher = twitter_data.TwitterFetcher()
given_id = 44196397 #Elon Musk

while True:

    elon_tweets = twitterFetcher.fetch(given_id)

    for tweet in elon_tweets.tweets:

        message = b"H" + bytes(str(tweet.to_repr()), "utf-8")
        producer.send("test-topic", key=b"python-message", value=message)
        print(f'Producing message @ {datetime.now()} | Message = {str(tweet.to_repr())}')
        time.sleep(2)
