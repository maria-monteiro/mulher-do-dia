import os
import tweepy

from dotenv import load_dotenv

load_dotenv()
client = tweepy.Client(
    consumer_key=os.getenv("CONSUMER_KEY"),
    consumer_secret=os.getenv("CONSUMER_SECRET"),
    access_token=os.getenv("ACCESS_TOKEN"),
    access_token_secret=os.getenv("ACCESS_TOKEN_SECRET")
)

user = client.get_user(username='MulherDoDia', user_auth=True)


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
mentions = client.get_users_mentions(user.data.id, since_id=last_seen_id, user_auth=True)

if mentions.data is not None:
    print(mentions.data)
    for data in reversed(mentions.data):  # reversed is for responding the older mentions first.
        print(str(data.id) + '---' + data.text)
        last_seen_id = data.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        print('Found MulherDoDia!')
        print('Responding back...')
        client.create_tweet(in_reply_to_tweet_id=last_seen_id, text='Testing', user_auth=True)
else:
    print('No new tweets have been found.')

