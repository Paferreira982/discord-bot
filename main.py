import sys
sys.path.insert(1, './local_lib')

import currency
from keep_alive import keep_alive
import discord
import os

client = discord.Client()

async def printMsg(string, message):
  await message.channel.send(string)

async def formatQuoteMsg(coin, message):
  usd = currency.getTokenQuote(coin)
  string = "{} \nUSD -> $  {:.2f} \nBRL  -> R$ {:.2f}".format(coin['symbol'], usd, currency.usdToBrl(usd))
  await printMsg(string, message)

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
    >
    > Retorna o valor do token em BRL e Dolar em tempo real
    > \t$bcoin
    > \t$thetan
    > \t$slp
    > \t$milk
    > \t$baby
    >
    > Converte um valor em token em BRL e Dolar
    > \t$convert [nome_token] [quantidade] -> Importante dar apenas "um espaço" entre os argumentos do comando.
    """
    await printMsg(string, message)

  if ()
  
  if msg.startswith("$bcoin") or msg.startswith("$BCOIN"):
    coin = {
      'slug': 'bombcrypto',
      'symbol': 'BCOIN'
    }
    await formatQuoteMsg(coin, message)
  
  if msg.startswith("$thetan") or msg.startswith("$THETAN"):
    coin = {
      'slug': 'thetan-coin',
      'symbol': 'THC'
    }
    await formatQuoteMsg(coin, message)
  
  if msg.startswith("$slp") or msg.startswith("$SLP"):
    coin = {
      'slug': 'smooth-love-potion',
      'symbol': 'SLP'
    }
    await formatQuoteMsg(coin, message)

  if msg.startswith("$milk") or msg.startswith("$MILK"):
    coin = {
      'slug': 'the-crypto-you',
      'symbol': 'MILK'
    }
    await formatQuoteMsg(coin, message)
  
  if msg.startswith("$baby") or msg.startswith("$BABY"):
    coin = {
      'slug': 'babyswap',
      'symbol': 'BABY'
    }
    await formatQuoteMsg(coin, message)

keep_alive()
client.run(os.environ['token'])