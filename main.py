import sys
sys.path.insert(1, './local_lib')

import currency
import discord
import os

client = discord.Client()

async def printMsg(string, message):
  await message.channel.send(string)

async def formatQuoteMsg(coin, message):
  usd = currency.getTokenQuote(coin)
  string = "{} \nUSD -> $  {:.2f} \nBRL  -> R$ {:.2f}".format(coin['symbol'], usd, currency.usdToBrl(usd))
  print(string)
  await printMsg(string, message)

@client.event
async def on_ready():
  print("Logado como {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith("$bcoin") or message.content.startswith("$BCOIN"):
    coin = {
      'slug': 'bombcrypto',
      'symbol': 'BCOIN'
    }
    await formatQuoteMsg(coin, message)
  
  if message.content.startswith("$thetan") or message.content.startswith("$THETAN"):
    coin = {
      'slug': 'thetan-coin',
      'symbol': 'THC'
    }
    await formatQuoteMsg(coin, message)
  
  if message.content.startswith("$slp") or message.content.startswith("$SLP"):
    coin = {
      'slug': 'smooth-love-potion',
      'symbol': 'SLP'
    }
    await formatQuoteMsg(coin, message)

client.run(os.environ['token'])