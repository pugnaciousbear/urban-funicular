import discord
import urllib.request
import asyncio
import time
import config
import datetime

list = config.bannedwords
admins = config.admins

def admins(message):
    if message.author.id in admins:
        return True
    else:
        return False

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
            if admins(message):
                await client.send_message(message.channel, ":wave:")
                await client.change_presence(game=discord.Game(name="Shutting down..."))
                print("Bot shutting down....")
                time.sleep(5)
                await client.logout()
                print("Bot has successfully shutdown")

            else:
                await client.send_message(message.channel, "Error: insufficient permission")

        if any(word in message.content for word in list):
            await client.delete_message(message)
            await client.kick(message.author)
            await client.send_message(message.channel, "The user was kicked for saying a banned word.")
            await client.send_message(message.author, "You were kicked from **LazyPurple's Discord Server** for saying a banned word.")
            print(message.author, "was kicked for saying ", message.content)

@client.event
async def on_server_available(server):
    print("Connected to", server)

@client.event
async def on_server_unavailable(server):
    print("Unable to connect to", server)

@client.event
async def on_server_join(server):
    print("WARNING: ADDED TO SERVER", server)




client.run(token)
