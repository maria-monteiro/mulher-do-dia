import os
import tweepy

from dotenv import load_dotenv

load_dotenv()

client = tweepy.Client(os.getenv('BEARER_TOKEN'))
user = client.get_user(username='MulherDoDia')
tweets = client.get_users_tweets(user.data.id)


FILE_NAME = 'last_seen_id.txt'


def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id


def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return


last_seen_id = retrieve_last_seen_id(FILE_NAME)
mentions = client.get_users_mentions(user.data.id, since_id=last_seen_id)

for data in reversed(mentions.data):  # reversed is for responding the older mentions first.
    print(str(data.id) + '---' + data.text)
    last_seen_id = data.id
    store_last_seen_id(last_seen_id, FILE_NAME)
    if '@MulherDoDia' in data.text:
        print('Found MulherDoDia!')
        print('Responding back...')
