import sys
sys.path.insert(1, './local_lib')

import commons
import currency
import discord
import os
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
  command = msg.split(" ")

  if msg.startswith("$help") or msg.startswith("$HELP"):
    string = """
    > COMANDOS
    > [token_name] -> Nome do token (bcoin, thetan, slp, milk, baby).
    > [quantity] -> Quantidade de token a converter.\n
    > Importante dar apenas "um espaço" entre os argumentos do comando.\n
    > Retorna o valor do token em BRL e Dolar em tempo real.
    > \t$price [token_name]\n
    > Converte um valor em token em BRL e Dolar.
    > \t$convert [token_name] [quantity]\n
    > Imprime a lista de tokens cadastrados.
    > \t$tokens
    """
    await commons.printMsg(string, message)

  if msg.startswith("$tokens"):
    await commons.printMsg("Tokens cadastrados: bcoin, thetan, slp, milk, baby", message)

  if msg.startswith("$convert"):
    await commons.printConvert(command, message)

  if msg.startswith("$price"):
    await commons.formatQuoteMsg(command, message)
  
keep_alive()
client.run(os.environ['token'])