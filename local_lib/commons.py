import discord
import currency

def getTokenInfo(tokenName):
    if tokenName == "bcoin":
        return {'slug': 'bombcrypto', 'symbol': 'BCOIN'}
    elif tokenName == "thetan":
        return {'slug': 'thetan-coin', 'symbol': 'THC'}
    elif tokenName == "slp":
        return {'slug': 'smooth-love-potion', 'symbol': 'SLP'}
    elif tokenName == "milk":
        return {'slug': 'the-crypto-you', 'symbol': 'MILK'}
    elif tokenName == "baby":
        return {'slug': 'babyswap', 'symbol': 'BABY'}
    elif tokenName == "all":
        return {'BCOIN','THC','SLP','MILK','BABY'}

async def printMsg(string, message):
    await message.channel.send(string)

async def printConvert(command, message):
    token = getTokenInfo(command[1])
    usd = currency.getTokenQuote(token)
    string = "```{} {}'s\nUSD ->  $ {:.2f}\nBRL -> R$ {:.2f}```".format(command[2], token['symbol'], usd*float(command[2]), currency.usdToBrl(usd)*float(command[2]))
    await printMsg(string, message)

async def printPrice(command, message):
    token = getTokenInfo(command[1])
    usd = currency.getTokenQuote(token)
    string = "```Valor atual do {}\nUSD ->  $ {:.2f}\nBRL -> R$ {:.2f}```".format(token['symbol'], usd, currency.usdToBrl(usd))
    await printMsg(string, message)

async def printTokens(message):
    string = "```Tokens cadastrados: "
    for tokenName in getTokenInfo("all"):
        string += tokenName.str.lower() + ", "
    string += "```"
    await printMsg(string, message)