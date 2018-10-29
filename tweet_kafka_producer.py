import sys
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import StreamListener
import json
import pykafka

class TweetsConsumer(StreamListener):

    def __init__(self, kafkaProducer):
        print("Procuce tweets")
        self.producer = kafkaProducer

    def on_data(self, raw_data):
        try:
            data_json = json.loads(raw_data)
            words = data_json["text"].split()
            lstHashTags = list(filter(lambda x: x.lower().startsWith("#"),words))
        except KeyError as e:
            print("Error in data %s"%str(e))
        return True

    def login_to_twitter(kafkaProducer, tracks):
        api_key = ""
        api_secret = ""

        access_token = ""
        access_token_secret = ""

        auth = OAuthHandler(api_key, api_secret)
        auth.set_access_token(access_token, access_token_secret)

        twitter_stream = Stream(auth, TweetsConsumer(kafkaProducer))
        twitter_stream.filter(tracks=tracks, languages=['en'])

    if __name__ == "__main__":
        if(len(sys.argv)<5):
            print("insufficient args", sys.stderr)
            exit(-1)

        host = sys.argv[1]
        port = sys.argv[2]
        topic = sys.argv[3]
        tracks = sys.argv[4]

        kafkaClient = pykafka.KafkaClient(host+":"+port)
        kafkaProducer = kafkaClient.topics[bytes(topic, "utf-8")].get_producer()
        login_to_twitter(kafkaProducer, tracks)
