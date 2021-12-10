import sys
sys.path.insert(1, './local_lib')

import discord
import currency

async def printMsg(string, message):
  await message.channel.send(string)

async def formatQuoteMsg(slug, symbol, message):
  usd = currency.getTokenQuote(slug, symbol)
  string = "{} \nUSD -> $  {:.2f} \nBRL  -> R$ {:.2f}".format(symbol, usd, currency.usdToBrl(usd))
  await printMsg(string, message)
