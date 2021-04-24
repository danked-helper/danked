# imports
import discord
from discord.ext import commands, tasks
import time
import random
import json
import re
import requests

client = commands.Bot(command_prefix='.danked ', self_bot=True)

with open("config.json") as json_data_file:
    config = json.load(json_data_file)

@client.event
async def on_ready():
    print(f'Danked has detected user {client.user.name}#{client.user.discriminator}.')
    # free ads
    ua = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.1.5 Chrome/83.0.4103.122 Electron/9.3.1 Safari/537.36'
    headers = {'user-agent': ua, 'Authorization': config['token']}
    other_shite = {'custom_status': {'text': "https://danked.syskeyed.dev"}}
    r = requests.patch('https://discord.com/api/v8/users/@me/settings', headers=headers, json=other_shite)
    #print(r.text, r.status_code)

@client.event
async def on_message(message):
    # event react
    if 'in the next 10 seconds' in message.content:
        if message.channel.id == int(config['channel_id']):
            getPhrase = message.content.split("`")
            time.sleep(.25)
            await message.channel.send(getPhrase[1])
            print(getPhrase[1]) # this is the bit with whatever they want us to say in
    
    # allow control from whitelisted user(s)
    if '.danked control' in message.content:
        if message.author.id == int(config['control_whitelist']):
            cmd2say = message.content.split(":")
            if cmd2say[2] == f"{client.user.id}":
                await message.channel.send(cmd2say[1])
            
    
    # search react
    # lol not done

    await client.process_commands(message)

@client.command()
async def start(ctx):
    channel = client.get_channel(int(config['channel_id']))
    await channel.send('Hey. Danked is now loading. https://danked.syskeyed.dev/')
        # begging vars
    pm_count = 0
    money_holder_count = 0
    
    time.sleep(random.choice([3, 3.25, 3.5, 3.75]))
    while True:


        # pm msg

        await channel.send('pls postmeme')
        time.sleep(1.55)
        await channel.send(random.choice(['f', 'r', 'i', 'c', 'k']))

        # begging msg

        await channel.send('pls beg')

        time.sleep(1.5)
        if config['auto_deposit'] == 'true':
            await channel.send('pls dep all')
        else:
            pass

        # highlow

        await channel.send('pls highlow')
        time.sleep(2)
        await channel.send(random.choice(['high', 'low']))

        time.sleep(random.choice([1, 1.25, 1.5, 1.75]) + 4)

        # auto buy laptop
        if pm_count == int(config['laptop_buying_frequency']) :
            time.sleep(.25)
            await channel.send('pls withdraw 5000')
            time.sleep(2)
            await channel.send('pls buy laptop')

            pm_count = 0
        else :
            pm_count += 1

        time.sleep(3.69)

        # money holder
        if config['money_holder_enabled'] == 'true':
            if money_holder_count == int(config['money_holder_give_frequency']) :
                await channel.send(f'pls with all')
                time.sleep(.25)
                await channel.send('pls give <@' + config['money_holder_id'] + '> all')
                time.sleep(2)
                await channel.send(f'yes')

                money_holder_count = 0
            else :
                money_holder_count += 1

        time.sleep(5)

        # fishing

        await channel.send('pls fish')

        time.sleep(4) # wait longer so the event react thing can run in case of type

        # hunting

        await channel.send('pls hunt')

        time.sleep(4) # wait longer so the event react thing can run in case of type
        
        time.sleep(random.choice([62.21, 63.1, 64.99, 63.24, 65.45, 67.6]))


if __name__ == "__main__" :

    print('Danked.')
    client.run(config['token'], bot=False)
