# imports
import discord
from discord.ext import commands, tasks
import time
import random
import requests
import json

client = commands.Bot(command_prefix='', self_bot=True)

@client.event
async def on_ready():
    print(f'Danked has detected user {client.user.name}#{client.user.discriminator}.')
    

@client.event
async def on_message(message):
    if message.content.startswith('grind'):
        await message.channel.send('Hey. Danked is now loading and will send messages in this channel.\nhaha syskeyed was here')
        # begging vars
        pm_count = 0
        #beg_count = 0
        # wait
        time.sleep(random.choice([3, 3.25, 3.5, 3.75]))
        while True:
            # fishing

            await message.channel.send('pls fish')

            time.sleep(1.5)

            # hunting

            await message.channel.send('pls hunt')

            time.sleep(1.5)

            # pm msg

            await message.channel.send('pls postmeme')
            time.sleep(1.55)
            await message.channel.send(random.choice(['f', 'r', 'i', 'c', 'k']))

            # begging msg

            await message.channel.send('pls beg')

            time.sleep(1.5)
            await message.channel.send('pls dep all')

            # highlow

            await message.channel.send('pls highlow')
            time.sleep(2)
            await message.channel.send(random.choice(['high', 'low']))

            time.sleep(random.choice([1, 1.25, 1.5, 1.75]) + 4)

            # auto buy laptop
            if pm_count == 50 :
                time.sleep(.25)
                await message.channel.send('pls withdraw 5000')
                time.sleep(2)
                await message.channel.send('pls buy laptop')

                pm_count = 0
            else :
                pm_count += 1

            time.sleep(random.choice([62.21, 63.1, 64.99, 63.24, 65.45, 67.6]))
       
if __name__ == "__main__" :  # we use this to run the script

    print('Danked.')
    print('Commands: \'grind\' - starts the bot.')
    tok = input('Enter your token here: ')
    client.run(f'{tok}', bot=False) 
    
