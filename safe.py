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


@client.event
async def on_message(message):
    # event react
    if 'in the next 10 seconds' in message.content:
        if message.channel.id == int(config['channel_id']):
            getPhrase = message.content.split("`")
            await asyncio.sleep(.25)
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

        # pm msg
        async with ctx.typing():
            type_time = random.uniform(0.5, 1)
            await asyncio.sleep(type_time)
        await channel.send('pls dig')

        await asyncio.sleep(random.uniform(.2, 1))

        # auto buy laptop
        if pm_count == int(config['laptop_buying_frequency']) :
            await asyncio.sleep(.25)
            async with ctx.typing():
                type_time = random.uniform(0.5, 1)
                await asyncio.sleep(type_time)

            await channel.send('pls withdraw 5000')

            await asyncio.sleep(random.uniform(.5, 2.4))

            async with ctx.typing():
                type_time = random.uniform(0.5, 1)
                await asyncio.sleep(type_time)

            await channel.send('pls buy laptop')

            pm_count = 0
        else :
            pm_count += 1
        # end auto laptop


        await asyncio.sleep(1.69)

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

                #await asyncio.sleep(.25)

                #async with ctx.typing():
                #    type_time = random.uniform(0.5, 1)
                #    await asyncio.sleep(type_time)
                #await channel.send('pls give <@' + config['money_holder_id'] + '> all')


                auto_lifesaver_count = 0
            else :
                auto_lifesaver_count += 1

        # fishing
        async with ctx.typing():
            type_time = random.uniform(0.5, 1)
            await asyncio.sleep(type_time)
        await channel.send('pls fish')

        await asyncio.sleep(random.uniform(4, 6)) # wait longer so the event react thing can run in case of type

        # hunting
        async with ctx.typing():
            type_time = random.uniform(0.5, 1)
            await asyncio.sleep(type_time)
        await channel.send('pls hunt')

        await asyncio.sleep(random.uniform(4, 6)) # wait longer so the event react thing can run in case of type
        
        await asyncio.sleep(random.uniform(45, 50))


if __name__ == "__main__" :

    print('Danked by syskeyed | 2021')
    client.run(config['token'], bot=False)
