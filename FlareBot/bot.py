import discord
import urllib.request
#import pynacl
#import libopus.dll
#import libopusurl.dll
#import opuslib.api.dexcoder
#import opuslib.api.encoder
#import opuslib.api.ctl
#import opuslib.constants
import asyncio
import time
import ffmpeg

client = discord.Client() #Defind 'client' this is what you'll use to have a chat with Discord!
token = config.apikey
print("Bot starting...")
musicURL = 'http://flare-radio.com:8000/stream'


@client.event
async def on_ready(): #Anything below is run when the bot logs into Discord's servers
    print("Logged into Discord. Loading Complete.")
    #await opus.load_opus()
    await client.change_presence(game=discord.Game(name="flare-radio.com"))

@client.event
async def on_message(message): #This is fired everytime a new message is sent either via PM or a server the bot is in. #message.content is a string of what the message is.
    if message.content.startswith("!hello"): #Check if the message begins with '!hello'
        await client.send_message(message.channel, ":wave: Hello there!") #Send a message to the channel the '!hello' message came from.

    if message.content.startswith(">shutdown"):
        await client.send_message(message.channel, ":wave:")
        await client.change_presence(game=discord.Game(name="Shutting down..."))
        print("Bot shutting down....")
        time.sleep(5)
        await client.logout()
        print("Bot has successfully shutdown")

    if message.content.startswith(">restart"):
        await client.run(token)
        await client.logout()
        await client.send_message(message.channel, "Restarting...")

    if message.content.startswith(">help"):
        await client.send_message(message.author, """```FlareRadio Discord Bot - Version 1.0

Website: http://flare-radio.com - Discord: http://discord.flare-radio.com

Commands:
     >help - Brings up this dialog
     >play - Plays the radio in your voice channel
     >info - Shows current song, presenter, volume and etc
     >version - Shows the bot version

More Commands Will Be Added Soon```""")

    if message.content.startswith(">version"):
        await client.send_message(message.author, """```Bot Information:
        Official FlareRadio Discord bot
        Version: 1.0
        Created by Geo```""")

    if message.content.startswith(">play"):
        c = discord.utils.get(message.server.channels, type=discord.ChannelType.voice)
        discord.opus.load_opus('C:\\Users\georg\OneDrive\Flare\opus.dll')
        voice = await client.join_voice_channel(c)
        player = voice.create_ffmpeg_player('http://flare-radio.com:8000/stream')
        player.start()
        #print(voiceclient)

#if message.content.startswith(">stop"):
#    voiceclient = await client.voice_client_in(message.server)
#    if voiceclient is None:
#        pass
#    else:
#        await voiceclient.disconnect()


@client.event
async def on_server_join(server):
    print("Added to server", server)

@client.event
async def on_server_remove(server):
    print("Removed from a server", server)

@client.event
async def on_server_available(server):
    print("GUILD AVAILABLE:", server)

@client.event
async def on_sever_unavailable(server):
    print("GUILD UNAVAILABLE:", server)

@client.event
async def on_server_update(before, after):
    print("Server Changed from", before, "to", after)


#voice = client.join_voice_channel(channel)
#player = voice.create_ffmpeg_player('http://sv.ggradio.net:8000/stream')
#player.start()


client.run(token)
