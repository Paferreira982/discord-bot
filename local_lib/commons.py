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

async def printHelp(message):
    string = """```Help
    \t[token_name] -> Nome do token.
    \t[quantity] -> Quantidade de token a converter.\n
    Comandos
    \t$price [token_name] -> Retorna o valor do token em BRL e Dolar em tempo real.
    \t$convert [quantity] [token_name] -> Converte um valor em token em BRL e Dolar.
    \t$tokens -> Imprime a lista de tokens cadastrados.
    ```"""
    await printMsg(string, message)

async def printPrice(command, message):
    token = getTokenInfo(command[1])
    usd = currency.getTokenQuote(token)
    string = "```Valor atual do {}\nUSD ->  $ {:.2f}\nBRL -> R$ {:.2f}```".format(token['symbol'], usd, currency.usdToBrl(usd))
    await printMsg(string, message)

async def printConvert(command, message):
    token = getTokenInfo(command[2].lower())
    usd = currency.getTokenQuote(token)
    string = "```{} {}'s\nUSD ->  $ {:.2f}\nBRL -> R$ {:.2f}```".format(command[1], token['symbol'], usd*float(command[1]), currency.usdToBrl(usd)*float(command[1]))
    await printMsg(string, message)

async def printTokens(message):
    string = "```Tokens cadastrados: "
    for tokenName in getTokenInfo("all"):
        string += tokenName.lower() + " "
    string += "```"
    await printMsg(string, message)