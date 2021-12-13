#Author: Pedro Augusto
#Lib commons: Biblioteca que guarda todas as funções que são utilizadas pelo script principal (main.py).
import discord
import currency
import riot_lib

helpString = """```
Help
\t[token_name]    -> Nome do token.
\t[quantity]      -> Quantidade de token a converter.
\t[summoner_name] -> Nome da conta de League of Legends.\n
Comandos NFT
\t$price    [token_name]              -> Retorna o valor do token em BRL e Dolar em tempo real.
\t$convert  [quantity] [token_name]   -> Converte um valor em token em BRL e Dolar.
\t$tokens                             -> Imprime a lista de tokens cadastrados.\n
Comandos League of Legends
\t$rank [summoner_name]  -> Retorna os ranks das filas flex e solo.```"""

#Função responsável por remover espaços duplos da mensagem do usuário e retorna uma array denominada "command".
def adjustCommand(msg):
    while("  " in msg):
        msg = msg.replace("  ", " ")
    return msg.split(" ")

#Função responsável por retornar informações necessárias para utilização das demais funções.
#Para cadastrar novos tokens, basta inserir nesta função.
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

#Função responsável por escrever uma mensagem já tratada no discord.
async def printMsg(string, message):
    await message.channel.send(string)

#Função responsável por escrever a mensagem do comando "$help"
async def printHelp(message):
    await printMsg(helpString, message)

#Função responsável por escrever a mensagem do comando "$price"
async def printPrice(command, message):
    token = getTokenInfo(command[1])
    usd = currency.getTokenQuote(token)
    string = "```Valor atual do {}\nUSD ->  $ {:.2f}\nBRL -> R$ {:.2f}```".format(token['symbol'], usd, currency.usdToBrl(usd))
    await printMsg(string, message)

#Função responsável por escrever a mensagem do comando "$convert"
async def printConvert(command, message):
    token = getTokenInfo(command[2].lower())
    usd = currency.getTokenQuote(token)
    string = "```{} {}'s\nUSD ->  $ {:.2f}\nBRL -> R$ {:.2f}```".format(command[1], token['symbol'], usd*float(command[1]), currency.usdToBrl(usd)*float(command[1]))
    await printMsg(string, message)

#Função responsável por escrever a mensagem do comando "$tokens"
async def printTokens(message):
    string = "```Tokens cadastrados: "
    for tokenName in getTokenInfo("all"):
        string += tokenName.lower() + " "
    string += "```"
    await printMsg(string, message)

def calculateWinRate(rank):
    return rank['wins'] * 100 / (rank['wins'] + rank['losses'])

def generateRankingString(rank):
    return "{} {} | {} PDL | WR {:.2f}%".format(rank['tier'], rank['rank'], rank['leaguePoints'], calculateWinRate(rank))

async def printLolRank(command, message):
    summonerName = command[1]
    if len(command) > 2:
        for i, arg in enumerate(command):
            summonerName += " " + command[i]
    
    ranks = riot_lib.getSummonerRank(riot_lib.getSummonerInfo(summonerName))
    string = "```"
    for rank in ranks:
        string += rank['summonerName']
        if rank['queueType'] == 'RANKED_SOLO_5x5':
            string += "\n\tSoloQ -> " + generateRankingString(rank)
        elif rank['queueType'] == 'RANKED_FLEX_SR':
            string += "\n\tFlex  -> " + generateRankingString(rank)
    string += "```"
    await printMsg(string, message)