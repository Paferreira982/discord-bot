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
    brl = currency.usdToBrl(usd)
    string = "Você possui ${:.2f} <> R${:.2f} em {}.".format(usd*int(command[2]), currency.usdToBrl(usd)*int(command[2]), token['symbol'])
    await printMsg(string, message)

async def formatQuoteMsg(command, message):
    token = getTokenInfo(command[1])
    usd = currency.getTokenQuote(token)
    string = "{} \nUSD -> $  {:.2f} \nBRL  -> R$ {:.2f}".format(token['symbol'], usd, currency.usdToBrl(usd))
    await printMsg(string, message)