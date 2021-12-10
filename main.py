import sys
sys.path.insert(1, './local_lib')

import currency
import discord
import os

client = discord.Client()

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

    usd = currency.getTokenQuote(coin)
    await message.channel.send("{} \nUSD -> $ {} \nBRL  -> R$ {}".format(coin['symbol'], usd, currency.usdToBrl(usd)))
  
  if message.content.startswith("$thetan") or message.content.startswith("$THETAN"):
    coin = {
      'slug': 'thetan-coin',
      'symbol': 'THC'
    }

    usd = currency.getTokenQuote(coin)
    await message.channel.send("{} \nUSD -> $ {} \nBRL  -> R$ {}".format(coin['symbol'], usd, currency.usdToBrl(usd)))

client.run(os.environ['token'])