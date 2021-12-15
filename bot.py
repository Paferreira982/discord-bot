# Author: PEDRO AUGUSTO
# Github: https://github.com/Paferreira982
# Description: Lib responsible for liscening main script.

import discord
import sys
import os
import asyncio

sys.path.insert(1, './local_lib')
import commons
import commands
from timer import Timer
from keep_alive import keep_alive

###########################
# CONFIGURATION VARIABLES #
###########################

# TIME IN MINUTES OF THE BOT STATUS CHANGE. 
statusInterval = 30

####################
# DISCORD COMMANDS #
####################

# RETURN THE DISCORD CLIENT. 
def getClient():
    try:
        return discord.Client()
    except Exception as e:
        print("[BOT] ERROR WHILE GETTING DISCORD CLIENT: {}".format(e).upper())

# GENERATES AN INTERVAL FOR CHANGING STATUS OVER THE TIME.    
def generateStatusLooping(client):
    try:
        Timer(interval=statusInterval*60, first_immediately=True, client=client, callback=commons.statusInterval)
    except Exception as e:
        print("[BOT] ERROR WHILE GENERATIONG STATUS LOOPING: {}".format(e).upper())

# EXECUTE SOME SCRIPTS AFTER THE SUCCESSFULLY LOGIN.
def ready(client):
    try:
        print("[BOT] LOGGED AS {0.user}".format(client).upper())
        generateStatusLooping(client)
    except Exception as e:
        print("[BOT] ERROR WHILE EXECUTING BOT READY: {}".format(e).upper())

# RESPONSIBLE FOR CALL THE SERVER AND RUN THE DISCORD BOT.
def run(client):
    keep_alive()
    client.run(os.environ['token'])
    loop = asyncio.get_event_loop()
    loop.run_forever()

# TRANSLATE THE COMMAND FROM USER TO A PADRONIZED OBJECT.
def getCommand(message):
    msg = message.content
    while("  " in msg):
        msg = msg.replace("  ", " ")

    arguments = msg.split(" ")
    del arguments[0]

    return {'arguments': arguments, 'message': message}

##################
# USER'S COMMANDS #
##################

async def help(command):
    return await commands.help(command)

async def price(command):
    return await commands.price(command)

async def convert(command):
    return await commands.convert(command)

async def tokens(command):
    return await commands.tokens(command)

async def rank(command):
    return await commands.rank(command)