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

  if msg.startswith("$help") or msg.startswith("$HELP"):
    string = """
    > COMANDOS
    > [token_name] -> Nome do token (bcoin, thetan, slp, milk, baby).
    > [quantity] -> Quantidade de token a converter.
    > Importante dar apenas "um espaço" entre os argumentos do comando.
    >
    > Retorna o valor do token em BRL e Dolar em tempo real.
    > \t$price [token_name] -> 
    >
    > Converte um valor em token em BRL e Dolar.
    > \t$convert [token_name] [quantity]
    """
    await commons.printMsg(string, message)

  if msg.startswith("$convert"):
    command = msg.split(" ")
    usd = currency.getTokenQuote(slug, symbol)

  if msg.startswith("$price"):
    commons.formatQuoteMsg(commons.getTokenInfo(command[2]), message)
  
  
  if msg.startswith("$bcoin") or msg.startswith("$BCOIN"):
    token = commons.getTokenInfo(command[2])
    commons.formatQuoteMsg('bombcrypto', 'BCOIN', message)
  
  if msg.startswith("$thetan") or msg.startswith("$THETAN"):
    commons.formatQuoteMsg('thetan-coin', 'THC', message)
  
  if msg.startswith("$slp") or msg.startswith("$SLP"):
    commons.formatQuoteMsg('smooth-love-potion', 'SLP', message)

  if msg.startswith("$milk") or msg.startswith("$MILK"):
    commons.formatQuoteMsg('the-crypto-you', 'MILK', message)
  
  if msg.startswith("$baby") or msg.startswith("$BABY"):
    commons.formatQuoteMsg('babyswap', 'BABY', message)
  
  

keep_alive()
client.run(os.environ['token'])