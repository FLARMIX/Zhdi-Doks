from config import *
from pyrogram import Client, filters
from pyrogram.types import Message
import random as rn

client = Client('telepython', api_id, api_hash)


def generate_message() -> str:
    message = 'abcdefgthojkl123456789@0p[]'
    test = [i for i in message]
    rn.shuffle(test)
    return ''.join(test)


@client.on_message(filters.regex('spam') & filters.me)
def spam(client, message: Message):
    try:
        x = 0
        while 10000 > x:
            msg = generate_message()
            client.send_message(message.chat.id, msg)
            x += 1
    except:
        return


client.run()
