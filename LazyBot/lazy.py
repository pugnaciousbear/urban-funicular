import discord
import urllib.request
import asyncio
import time
import config

list = ['banned', 'words']

client = discord.Client()
token = config.apikey
print("Bot starting...")

@client.event
async def on_ready(): #Anything below is run when the bot logs into Discord's servers
    print("Logged into Discord. Loading Complete.")
    #await opus.load_opus()
    await client.change_presence(game=discord.Game(name="LazyPurple"))

@client.event
async def on_message(message):
        if message.content.startswith(">shutdown"):
            await client.send_message(message.channel, ":wave:")
            await client.change_presence(game=discord.Game(name="Shutting down..."))
            print("Bot shutting down....")
            time.sleep(5)
            await client.logout()
            print("Bot has successfully shutdown")

client.run(token)
