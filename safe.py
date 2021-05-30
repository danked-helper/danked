# imports
import discord
from discord.ext import commands, tasks
import asyncio
import random
import json
import re
import requests

client = commands.Bot(command_prefix='.danked ', self_bot=True)

with open("config.json") as json_data_file:
    config = json.load(json_data_file)

with open("auto-sell.json") as json_data_file2:
    autosell = json.load(json_data_file2)

@client.event
async def on_ready():
    print(f'Danked has detected user {client.user.name}#{client.user.discriminator}.')

@client.command()
async def start(ctx):
    channel = client.get_channel(int(config['channel_id']))
    print('Starting...')
        # begging vars
    pm_count = 0
    money_holder_count = 0
    auto_lifesaver_count = 0
    
    await asyncio.sleep(2)

    async with ctx.typing():
        type_time = random.uniform(0.5, 1)
        await asyncio.sleep(type_time)            
    await channel.send('pls settings confirmations false')

    while True:

        # pm msg
        async with ctx.typing():
            type_time = random.uniform(0.5, 1)
            await asyncio.sleep(type_time)
        await channel.send('pls postmeme')

        async with ctx.typing():
            type_time = random.uniform(0.5, .7)
            await asyncio.sleep(type_time)
        await channel.send(random.choice(['f', 'r', 'i', 'c', 'k']))

        # begging msg
        async with ctx.typing():
            type_time = random.uniform(0.5, 3)
            await asyncio.sleep(type_time)
        await channel.send('pls beg')

        await asyncio.sleep(random.uniform(1.34, 3.47))

        if config['auto_deposit'] == 'true':

            async with ctx.typing():
                type_time = random.uniform(0.5, 3.5)
                await asyncio.sleep(type_time)

            await channel.send('pls dep all')
        else:
            pass
        
        # auto sell

        # highlow
        async with ctx.typing():
            type_time = random.uniform(0.4, 4)
            await asyncio.sleep(type_time)
        await channel.send('pls highlow')

        await asyncio.sleep(random.uniform(.2, 1))


        async with ctx.typing():
            type_time = random.uniform(0.5, 1)
            await asyncio.sleep(type_time)
        await channel.send(random.choice(['high', 'low']))

        await asyncio.sleep(random.uniform(1,3))

        # dig
        async with ctx.typing():
            type_time = random.uniform(0.5, 1)
            await asyncio.sleep(type_time)
        await channel.send('pls dig')

        await asyncio.sleep(random.uniform(.2, 1))

        # money holder
        if config['money_holder_enabled'] == 'true':
            if money_holder_count == int(config['money_holder_give_frequency']) :
                async with ctx.typing():
                    type_time = random.uniform(0.5, 1)
                    await asyncio.sleep(type_time)
                await channel.send(f'pls with all')

                await asyncio.sleep(.25)

                async with ctx.typing():
                    type_time = random.uniform(0.5, 1)
                    await asyncio.sleep(type_time)
                await channel.send('pls give <@' + config['money_holder_id'] + '> all')


                money_holder_count = 0
            else :
                money_holder_count += 1

        await asyncio.sleep(1)

        # auto lifesaver
        if config['auto_lifesaver_enabled'] == 'true':
            if auto_lifesaver_count == int(config['auto_lifesaver_frequency']) :
                async with ctx.typing():
                    type_time = random.uniform(0.5, 1)
                    await asyncio.sleep(type_time)
                await channel.send(f'pls use lifesaver')

                auto_lifesaver_count = 0
            else :
                auto_lifesaver_count += 1

        # fishing
        async with ctx.typing():
            type_time = random.uniform(0.5, 1)
            await asyncio.sleep(type_time)
        await channel.send('pls fish')

        await asyncio.sleep(random.uniform(1, 2))

        # hunting
        async with ctx.typing():
            type_time = random.uniform(0.5, 1)
            await asyncio.sleep(type_time)
        await channel.send('pls hunt')

        await asyncio.sleep(random.uniform(1, 2))
        
        await asyncio.sleep(random.uniform(45, 50))


if __name__ == "__main__" :

    print('Danked by syskeyed | 2021')
    client.run(config['token'], bot=False)
