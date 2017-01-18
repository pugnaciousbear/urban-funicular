import discord
import asyncio
import time
import random
import config
admins = config.admins
bannedwords = config.bannedwords
def admin(message):
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
        if admin(message):
            await client.send_message(message.channel, ":wave:")
            await client.change_presence(game=discord.Game(name="Shutting down..."))
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx            print("Bot shutting down on request of user", message.author, ".....")
            time.sleep(5)
            await client.logout()
            print("Bot has successfully shutdown.")

        else:
            print("User", message.author, "tried to shut down the bot!")

    if any(word in message.content for word in bannedwords):
        await client.delete_message(message)
        await client.kick(message.author)
        await client.send_message(message.channel, "The user was kicked for saying a banned word.")
        await client.send_message(message.author, "You were kicked from **LazyPurple's Discord Server** for saying a banned word.")
        print(message.author, "was kicked for saying ", message.content)

    if message.content.startswith(">servers"):
        if admin(message):
            servers = list(client.servers)
            listsrv = []
            for i in servers:
                listsrv.append(i.name)
                listsrv.append(i.id)
            await client.send_message(message.author, "```[servername, serverid] \n " + str(listsrv) + "\n```")

@client.event
async def on_server_available(server):
    print("Connected to", server)

@client.event
async def on_server_unavailable(server):
    print("Unable to connect to", server)

@client.event
async def on_server_join(server):
    print("WARNING: ADDED TO SERVER", server)



def run():
    client.run(token)

run()
