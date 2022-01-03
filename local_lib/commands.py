# Author: PEDRO AUGUSTO
# Github: https://github.com/Paferreira982
# Description: Lib responsible for executing commands in discord.

import discord
import commons

###########################
# CONFIGURATION VARIABLES #
###########################

# THE STRING THAT IS PRINTED IN '$help' COMMAND.
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

#######################
# UTILITIES FUNCTIONS #
#######################

# ADD A TEXT COMMAND TO BEAUTY THE STRING.
def beautyString(string):
    return string + "```"

# RETURNS AN INFORMATION ABOUT A TOKEN.
# YOU CAN SAVE NEW TOKENS BY ADD IN THIS METHOD.
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

# MAKE THE DISCORD BOT WRITE AN MESSAGE.
async def printMsg(string, command):
    try:
        await command['message'].channel.send(string)
    except Exception as e:
        print("[BOT] ERROR WHILE PRINTING MESSAGE IN DISCORD: {}".format(e).upper())

# CALCULATE THE WIN RATE.
def calculateWinRate(rank):
    return rank['wins'] * 100 / (rank['wins'] + rank['losses'])

# GENERATE A STRING FROM '$rank' COMMAND.
def generateRankingString(rank):
    return "{} {} | {} PDL | WinRate {:.2f}%".format(rank['tier'], rank['rank'], rank['leaguePoints'], calculateWinRate(rank))

##################
# STATUS COMMAND #
##################

async def changeStatus(client, status):
    try:
        await client.change_presence(activity=discord.Game(name=status))
    except Exception as e:
        print("[BOT] STATUS NÃO ATUALIZADO: {}".format(e))

####################
# SIMPLES COMMANDS #
####################

# EXECUTE THE '$help' COMMAND.
async def help(command):
    print("[BOT] EXECUTING '$help' COMMAND")
    await printMsg(helpString, command)

################
# NFT COMMANDS #
################ 

# EXECUTE THE '$price' COMMAND.
async def price(command):
    try:
        print("[BOT] EXECUTING '$price' COMMAND")
        arguments = command['arguments']
        string = beautyString("")

        for arg in arguments:
            coin = getTokenInfo(arg)

            if coin is not None:
                usd = commons.getTokenQuote(coin)
                string += "\nValor atual do {}".format(coin['symbol'])
                string += "\nUSD ->  $ {:.2f}\nBRL -> R$ {:.2f}\n".format(usd, commons.usdToBrl(usd))
            else:
                string = beautyString("")
                string += "Token {} não existente/cadastrado.".format(arg)
                break

        string = beautyString(string)
        await printMsg(string, command)

    except Exception as e:
        print("[BOT] ERROR WHILE RUNNING COMMAND '$price': {}".format(e).upper())

# EXECUTE THE '$convert' COMMAND.
async def convert(command):
    try:
        print("[BOT] EXECUTING '$convert' COMMAND")
        arguments = command['arguments']
        string = beautyString("")
        if len(arguments) == 2:
            coin = getTokenInfo(arguments[1].lower())

            if coin is not None:
                usd = commons.getTokenQuote(coin)
                if arguments[0].isnumeric():
                    string += "{} {}'s\nUSD ->  $ {:.2f}\nBRL -> R$ {:.2f}".format(arguments[0], coin['symbol'], usd*float(arguments[0]), commons.usdToBrl(usd)*float(arguments[0]))
                else:
                    string += "O argumento [quantity] precisa ser preenchido com um número."
            else:
                string += "Token {} não existente/cadastrado.".format(arguments[0])

        else:
            string += 'Argumentos insuficientes para o comando "$convert".'

        string = beautyString(string)
        await printMsg(string, command)

    except Exception as e:
        print("[BOT] ERROR WHILE RUNNING COMMAND '$convert': {}".format(e).upper())

# EXECUTE THE '$tokens' COMMAND.
async def tokens(command):
    try:
        print("[BOT] EXECUTING '$tokens' COMMAND")
        string = beautyString("")
        string += "Tokens cadastrados \n"

        for tokenName in getTokenInfo("all"):
            string += tokenName.lower() + " "

        string = beautyString(string)
        await printMsg(string, command)

    except Exception as e:
        print("[BOT] ERROR WHILE RUNNING COMMAND '$tokens': {}".format(e).upper())

##############################
# LEAGUE OF LEGENDS COMMANDS #
############################## 

# EXECUTE THE '$rank' COMMAND.
async def rank(command):
    try:
        print("[BOT] EXECUTING '$rank' COMMAND")
        arguments = command['arguments']
        summonerName = arguments[0]

        if len(arguments) > 1:
            for i, arg in enumerate(arguments):
                if i > 0:
                    summonerName += " " + arg

        ranks = commons.getSummonerRank(commons.getSummonerInfo(summonerName))
        string = beautyString("")

        if ranks is not None:
            string += summonerName + " "
            for rank in ranks:
                if rank['queueType'] == 'RANKED_SOLO_5x5':
                    string += "\n\tSoloQ -> " + generateRankingString(rank)
                elif rank['queueType'] == 'RANKED_FLEX_SR':
                    string += "\n\tFlex  -> " + generateRankingString(rank)
        else:
            string += "Summoner {} não encontrado.".format(summonerName.strip())

        string = beautyString(string)
        await printMsg(string, command)

    except Exception as e:
        print("[BOT] ERROR WHILE RUNNING COMMAND '$rank': {}".format(e).upper())
    