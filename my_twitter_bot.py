import os
import tweepy

from dotenv import load_dotenv

load_dotenv()

client = tweepy.Client(os.getenv('BEARER_TOKEN'))
user = client.get_user(username='ashra43')
tweets = client.get_users_tweets(user.data.id)
for data in tweets.data:
    print(data.text)




