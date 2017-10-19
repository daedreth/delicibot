#!/usr/bin/env python3

import asyncio
import discord
import configparser
import os

# Global
client = discord.Client()
config = configparser.ConfigParser()
config.read(os.environ['HOME'] + '/.config/umadelicia/config.ini')

@client.event
async def on_ready():
    print('Connected!')
    print('Monitoring for: ' + client.user.name)

@client.event
async def on_message(message):
    if message.content == 'UMA' and message.author != client.user:
        await client.send_message(message.channel, 'DELICIA')
        print('Answered: ' + message.author.name)

if __name__ == '__main__':
    print('Connecting...')
    client.run(config['Main']['token'], bot=False)
