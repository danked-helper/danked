import discord
from discord.ext import commands, tasks
import asyncio
import random
import json
import re
import requests

with open("config.json") as json_data_file:
    config = json.load(json_data_file)

listener = commands.Bot(command_prefix='msg')

def force_msg(msg, channelid, token):
    headers = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0",
        "Authorization" : f"{token}"
    }
    payload = {
        "content":f"{msg}","nonce":"","tts":"false" # DONT SEND A NONCE I WASTED 4 HOURS ON THIS
    }
    send = requests.post(f"https://discord.com/api/v9/channels/{channelid}/messages", headers=headers, json=payload)
    #print(send.text)

@listener.event
async def on_ready():
    print(f'Danked has detected bot {listener.user.name}#{listener.user.discriminator}.')

@listener.event
async def on_message(message):
    # event react
    if 'Type the phrase below in the next 10 seconds' in str(message.content):
        if message.channel.id == int(config['channel_id']):
            getPhrase = message.content.split("`")
            force_msg(f'{getPhrase[1]}', str(config['channel_id']), str(config['token']))

    
    elif 'Quickly reverse the word' in message.content:
        if message.channel.id == int(config['channel_id']):
            getPhrase = message.content.split("`")[1]
            reversePhrase = str(getPhrase)[::-1]
            force_msg(f'{reversePhrase}', str(config['channel_id']), str(config['token']))

    
    elif '**Laptop** is broken lmao' in message.content:
        if message.channel.id == int(config['channel_id']):
            force_msg('pls buy laptop', config['channel_id'], config['token'])

    # allow control from whitelisted user(s)
    #elif '.danked control' in message.content:
    #    if message.author.id == int(config['control_whitelist']):
    #        cmd2say = message.content.split(":")
    #        if cmd2say[2] == f"{listener.user.id}":
    #            await message.channel.send(cmd2say[1])

    else: 
        pass
            
    # search react
    # lol not done

    await listener.process_commands(message)


listener.run(config['react_bot_token'])
