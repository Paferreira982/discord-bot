import sys
sys.path.insert(1, './local_lib')

import discord
import currency

async def printMsg(string, message):
    await message.channel.send(string)

async def formatQuoteMsg(token, message):
    usd = currency.getTokenQuote(token)
    string = "{} \nUSD -> $  {:.2f} \nBRL  -> R$ {:.2f}".format(token['symbol'], usd, currency.usdToBrl(usd))
    await printMsg(string, message)

def getTokenInfo(token):
    if token == "bcoin":
        return {'slug': 'bombcrypto', 'symbol': 'BCOIN'}
    elif token == "thetan":
        return {'slug': 'thetan-coin', 'symbol': 'THC'}
    elif token == "slp":
        return {'slug': 'smooth-love-potion', 'symbol': 'SLP'}
    elif token == "milk":
        return {'slug': 'the-crypto-you', 'symbol': 'MILK'}
    elif token == "baby":
        return {'slug': 'babyswap', 'symbol': 'BABY'}