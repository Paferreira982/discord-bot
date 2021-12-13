#Author: Pedro Augusto
#Script principal: Gerencia os comandos proveniente do usuário.
import sys
import os
import asyncio

#Insere a pasta "local_lib" no path do sistema, para tornar os scripts presentes visíveis.
sys.path.insert(1, './local_lib')

import discord
import commons
from timer import Timer
from keep_alive import keep_alive

client = discord.Client()
timer1 = Timer(interval=1200, first_immediately=True, client=client, callback=commons.statusInterval)

#Função responsável por informar se o login no BOT foi bem sucedido.
@client.event
async def on_ready():
  print("Logado como {0.user}".format(client))
  
#Função responsável por capturar a input do usuário e identificar qual comando foi enviado.
@client.event
async def on_message(message):
  #Encerra a verificação da input, caso a mensagem do sistem seja proveniente do BOT.
  if message.author == client.user and not message.content.startswith("$"):
    return

  msg = message.content.strip()
  command = commons.adjustCommand(msg)

  if len(command) > 1:
    if msg.startswith("$convert"):
      await commons.printConvert(command, message)

    if msg.startswith("$price"):
      await commons.printPrice(command, message)
  
    if msg.startswith("$rank"):
      await commons.printLolRank(command, message)
  else:
    if msg.startswith("$help"):
      await commons.printHelp(message)

    if msg.startswith("$tokens"):
      await commons.printTokens(message)

loop = asyncio.get_event_loop()
loop.run_forever()

keep_alive()
client.run(os.environ['token'])