#Author: Pedro Augusto
#Lib commons: Biblioteca que guarda todas as funções que são utilizadas pelo script principal (main.py).
import discord
import threading
import random

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
    if tokenName == "thetan":
        return {'slug': 'thetan-coin', 'symbol': 'THC'}
    if tokenName == "slp":
        return {'slug': 'smooth-love-potion', 'symbol': 'SLP'}
    if tokenName == "milk":
        return {'slug': 'the-crypto-you', 'symbol': 'MILK'}
    if tokenName == "baby":
        return {'slug': 'babyswap', 'symbol': 'BABY'}
    if tokenName == "all":
        return ['BCOIN','THC','SLP','MILK','BABY']
    return None

def getRandomStatusString():
    tokens = getTokenInfo("all")
    i = random.randint(0,len(tokens))

    coin = getTokenInfo(tokens[i].lower())
    token_id = currency.getId(coin)

    token = currency.getTokenInfo(coin)
    usd = currency.getTokenQuote(token, token_id)

    dailyChange = float(token['data'][token_id]['quote']['USD']['percent_change_24h'])
    return "{} -> R$ {:.2f} | {:.2f}%".format(coin['symbol'], currency.usdToBrl(usd), dailyChange)

async def statusInterval(client):
    await client.change_presence(activity=discord.Game(name=getRandomStatusString()))

#Função responsável por escrever uma mensagem já tratada no discord.
async def printMsg(string, message):
    await message.channel.send(string)

#Função responsável por escrever a mensagem do comando "$help"
async def printHelp(message):
    await printMsg(helpString, message)

#Função responsável por escrever a mensagem do comando "$price"
async def printPrice(command, message):
    token = getTokenInfo(command[1])
    string = ""

    if token is not None:
        usd = currency.getTokenQuote(token)
        string = "```Valor atual do {}\nUSD ->  $ {:.2f}\nBRL -> R$ {:.2f}```".format(token['symbol'], usd, currency.usdToBrl(usd))
    else:
        string = "Token {} não existente/cadastrado.".format(command[1])

    await printMsg(string, message)

#Função responsável por escrever a mensagem do comando "$convert"
async def printConvert(command, message):
    string = ""
    if len(command) != 3:
        string = 'Argumentos insuficientes para o comando "$convert".'
    else:
        token = getTokenInfo(command[2].lower())

        if token is not None:
            usd = currency.getTokenQuote(token)
            if command[1].isnumeric():
                string = "```{} {}'s\nUSD ->  $ {:.2f}\nBRL -> R$ {:.2f}```".format(command[1], token['symbol'], usd*float(command[1]), currency.usdToBrl(usd)*float(command[1]))
            else:
                string = "O argumento [quantity] precisa ser preenchido com um número."
        else:
            string = "Token {} não existente/cadastrado.".format(command[2])

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
    return "{} {} | {} PDL | WinRate {:.2f}%".format(rank['tier'], rank['rank'], rank['leaguePoints'], calculateWinRate(rank))

async def printLolRank(command, message):
    summonerName = command[1]

    if len(command) > 2:
        for i, arg in enumerate(command):
            if i > 1:
                summonerName += " " + arg

    ranks = riot_lib.getSummonerRank(riot_lib.getSummonerInfo(summonerName))
    string = "```"

    if ranks is not None:
        string += summonerName
        for rank in ranks:
            if rank['queueType'] == 'RANKED_SOLO_5x5':
                string += "\n\tSoloQ -> " + generateRankingString(rank)
            elif rank['queueType'] == 'RANKED_FLEX_SR':
                string += "\n\tFlex  -> " + generateRankingString(rank)
    else:
        string += "Summoner {} não encontrado.".format(summonerName)

    string += "```"
    await printMsg(string, message)