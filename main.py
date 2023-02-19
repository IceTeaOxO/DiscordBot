# This example requires the 'message_content' intent.

import discord
import os
from dotenv import load_dotenv
import requests
import OpenAI.main as mainAPI
load_dotenv()

TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # chatGPT
    if message.content.startswith("%"):
        try:
            text = mainAPI.chatAPI(message.content[1:])
            # print(message.content[1:])
            print(text)
            await message.channel.send(text)
        except:
            await message.channel.send("忙碌中，等等再來找我聊天叭")
    # drawAPI
    if message.content.startswith("*"):
        try:
            url = mainAPI.imageAPI(message.content[1:])
            # print(message.content[1:])
            # print(url)
            await message.channel.send(url)
        except:
            await message.channel.send("不咳以瑟瑟")
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
        
    if message.content.startswith("req"):
        x = requests.get('http://127.0.0.1:8000/')
        print(x.text)
        await message.channel.send('req')

client.run(TOKEN)