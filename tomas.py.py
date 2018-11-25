import discord
import youtube_dl
from discord.ext import commands

TOKEN = "NTAyMjI2MDYzNzYyMzkxMDUw.Dqk38g.KFDtyaHwMfRNK6RRUKYfpDj9L9Y"

musicBot = commands.Bot(command_prefix ="!")


players = {} #It allows to store the player of each server, so that you can access them when people run comannds like pause,resume,stop.
queues = {} #It allows to store a bucnh of queues and access them using a server id as the key.

""" This function checks if there is an existing song in the queue, if
    there is it pops it off out of the queue and plays it right away"""
def check_queue(id):
    if queues[id] != []:
        player = queues[id].pop(0)
        players[id] = player
        player.start()
        
"""It creates a function to detects when the bot is ready or when it is done to collect all the information from discord"""
@musicBot.event
async def on_ready():
    print("Music Bot is ready.")

"""This command allows the bot to join the voice channel"""
@musicBot.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    if channel:
        await musicBot.join_voice_channel(channel)
        await musicBot.say("You joined the channel" )
    else:
        await musicBot.say("Try again, not connected to the channel")

"""This command allows the bot to leave the voice channel"""
@musicBot.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = musicBot.voice_client_in(server)
    if voice_client:
        await voice_client.disconnect()
        await musicBot.say("You left the voice channel")
    else:
        await musicBot.say("You are not in the channel")

"""This command allows the bot to play a music of a given name in the voice channel"""
@musicBot.command(pass_context=True)
async def play(ctx, url):
    server = ctx.message.server
    voice_client = musicBot.voice_client_in(server)
    if voice_client:
        """When someone creates a player it will either add server's player to
           our list of players(players ={}) or update the existing one"""
        player = await voice_client.create_ytdl_player(url, ytdl_options={'default_search': 'auto'}, after=lambda: check_queue(server.id))
        players[server.id] = player
        player.start()
        await musicBot.say("Playing music. ")
    else:
        await musicBot.say("Music not recognized.")

"""This command allows the bot to pause a music in the voice channel"""
@musicBot.command(pass_context=True)
async def pause(ctx):
    id= ctx.message.server.id
    await musicBot.say('Music is paused.')
    players[id].pause()
    
"""This command allows the bot to resume a music in the voice channel"""    
@musicBot.command(pass_context=True)
async def resume(ctx):
    id= ctx.message.server.id
    await musicBot.say("Music is resumed.")
    players[id].resume()

"""This command allows the bot to stop a music in the voice channel"""
@musicBot.command(pass_context=True)
async def stop(ctx):
    id= ctx.message.server.id
    await musicBot.say("Music is stopped.")
    players[id].stop()


"""This command allows the bot to play a sort of next song that you have stored in a queue as soon of the fisrt song is ended of a given name in the voice channel"""
@musicBot.command(pass_context=True)
async def queue(ctx, url):
    server = ctx.message.server
    voice_client = musicBot.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url, ytdl_options={'default_search': 'auto'}, after=lambda: check_queue(server.id))
    
    if server.id in queues: # if there is an existing queue put the player at the end of the queue.
        queues[server.id].append(player)
    else: # if there is not an existing queue.
        queues[server.id] = [player]
    await musicBot.say("Music is queued.")
        
    
musicBot.run(TOKEN)
