# imports
import discord
from discord.ext import commands, tasks
import time
import random
import json

client = commands.Bot(command_prefix='.danked', self_bot=True)

with open("config.json") as json_data_file:
    config = json.load(json_data_file)


@client.event
async def on_ready():
    print(f'Danked has detected user {client.user.name}#{client.user.discriminator}.')
    

@client.command()
async def start(ctx):
    channel = client.get_channel(int(config['channel_id']))
    await channel.send('Hey. Danked is now loading. https://danked.syskeyed.dev/')
        # begging vars
    pm_count = 0
    money_holder_count = 0
    
    time.sleep(random.choice([3, 3.25, 3.5, 3.75]))
    while True:
        # fishing

        await channel.send('pls fish')

        time.sleep(1.5)

        # hunting

        await channel.send('pls hunt')

        time.sleep(1.5)

        # pm msg

        await channel.send('pls postmeme')
        time.sleep(1.55)
        await channel.send(random.choice(['f', 'r', 'i', 'c', 'k']))

        # begging msg

        await channel.send('pls beg')

        time.sleep(1.5)
        await channel.send('pls dep all')

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
                time.sleep(.25)
                await channel.send(f'pls give <@{int(config['money_holder_id'])} all')
                time.sleep(2)
                await channel.send(f'yes')

                money_holder_count = 0
            else :
                money_holder_count += 1
        
        time.sleep(random.choice([62.21, 63.1, 64.99, 63.24, 65.45, 67.6]))


if __name__ == "__main__" :

    print('Danked.')
    client.run(config['token'], bot=False) 
    
