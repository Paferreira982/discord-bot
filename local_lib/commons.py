import discord
import currency

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

async def printMsg(string, message):
    await message.channel.send(string)

async def printConvert(command, message):
    token = getTokenInfo(command[1])
    usd = currency.getTokenQuote(token)
    string = "Convertendo {} {}'s\nUSD -> $  {:.2f} \nBRL  -> R$ {:.2f}".format(command[2], token['symbol'], usd*float(command[2]), currency.usdToBrl(usd)*float(command[2]))
    await printMsg(string, message)

async def formatQuoteMsg(command, message):
    token = getTokenInfo(command[1])
    usd = currency.getTokenQuote(token)
    string = "{} \nUSD -> $  {:.2f} \nBRL  -> R$ {:.2f}".format(token['symbol'], usd, currency.usdToBrl(usd))
    await printMsg(string, message)