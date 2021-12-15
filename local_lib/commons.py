# Author: PEDRO AUGUSTO
# Github: https://github.com/Paferreira982
# Description: Lib responsible for connect all libs with methods.

import discord
import random

import currency
import riot_lib
import commands

##################
# COMMON METHODS #
##################

def getRandomStatusString():
    tokens = commands.getTokenInfo("all")
    i = random.randint(0,len(tokens)-1)

    coin = commands.getTokenInfo(tokens[i].lower())
    print("[BOT] CHANGING STATUS TO {}".format(coin['symbol']))

    token_id = currency.getId(coin)

    token = currency.getTokenInfo(coin)
    usd = currency.getQuote(token, token_id)

    dailyChange = float(token['data'][token_id]['quote']['USD']['percent_change_24h'])
    return "{} R$ {:.2f} | {:.2f}%".format(coin['symbol'], currency.usdToBrl(usd), dailyChange)

async def statusInterval(client):
    try:
        await client.change_presence(activity=discord.Game(name=getRandomStatusString()))
    except Exception as e:
        print("[BOT] STATUS NÃO ATUALIZADO: {}".format(e))

##############################
# COMMUNICATION BETWEEN LIBS #
##############################

def usdToBrl(usd):
    return currency.usdToBrl(usd)

def getTokenQuote(token):
    return currency.getTokenQuote(token)

def getSummonerRank(summoner):
    return riot_lib.getSummonerRank(summoner)

def getSummonerInfo(summonerName):
    return riot_lib.getSummonerInfo(summonerName)