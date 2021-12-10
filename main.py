import sys
sys.path.insert(1, './lib')

import currency
import discord
import os


print(currency.USDToBRL(1))
client = discord.Client()

@client.event
async def on_ready():
  print("Logado como {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith("$ola"):
    await message.channel.send("Olá!")

client.run(os.environ['token'])