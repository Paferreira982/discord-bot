import sys
sys.path.insert(1, './local_lib')

import discord
import currency

async def printMsg(string, message):
  await message.channel.send(string)

async def formatQuoteMsg(slug, symbol, message):
  coin = {
    'slug': slug,
    'symbol': symbol
  }

  usd = currency.getTokenQuote(coin)
  string = "{} \nUSD -> $  {:.2f} \nBRL  -> R$ {:.2f}".format(coin['symbol'], usd, currency.usdToBrl(usd))
  await printMsg(string, message)