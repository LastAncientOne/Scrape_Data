# Twitter Library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Twitter information
CONSUMER_KEY = '****' # **** input
CONSUMER_SECRET =  '****' # **** input
ACCESS_KEY =  '****' # **** input
ACCESS_SECRET =  '****' # **** input

# https://www.pythoncentral.io/introduction-to-tweepy-twitter-for-python/
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    # Twitter authetification and connection to Twiter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    stream = Stream(auth, l)

    # Twitter Streams to capture data Keywords
    stream.filter(track=['uphappy', 'depression', 'anxiety', 'mental health', 'suicide', 'suicidal', 'stress', 'sad', 'sadness'])
