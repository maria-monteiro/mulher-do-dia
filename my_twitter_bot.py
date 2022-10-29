import os
import tweepy

from dotenv import load_dotenv

load_dotenv()

client = tweepy.Client(os.getenv('BEARER_TOKEN'))
user = client.get_user(username='MulherDoDia')
tweets = client.get_users_tweets(user.data.id)
mentions = client.get_users_mentions(user.data.id)
for data in mentions.data:
    # print(str(data.id) + data.text)
    if '@MulherDoDia'.lower() in data.text.lower():
        print(data.text)










