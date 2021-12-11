import sys
import os
sys.path.insert(1, './local_lib')

import commons
import discord
from keep_alive import keep_alive

client = discord.Client()

#eventos do client do discord
@client.event
async def on_ready():
  print("Logado como {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user and not message.content.startswith("$"):
    return

  msg = message.content
  command = msg.replace("  ","").split(" ")
  print(command)

  if msg.startswith("$help") or msg.startswith("$HELP"):
    await commons.printHelp(message)

  if msg.startswith("$tokens"):
    await commons.printTokens(message)

  if msg.startswith("$convert"):
    await commons.printConvert(command, message)

  if msg.startswith("$price"):
    await commons.printPrice(command, message)
  
keep_alive()
client.run(os.environ['token'])