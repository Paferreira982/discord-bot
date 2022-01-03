# Author: PEDRO AUGUSTO
# Github: https://github.com/Paferreira982
# Description: Lib responsible for connect all libs with methods.

import discord
import random

import currency
import riot_lib
import commands

from timer import Timer

###########################
# CONFIGURATION VARIABLES #
###########################

tokens = commands.getTokenInfo("all")
statusTimer = None
i = None

##################
# COMMON METHODS #
##################

def getCoin():
    global i

    if i is None:
        i = random.randint(0,len(tokens)-1)
    else:
        aux = i
        while aux == i:
            aux = random.randint(0,len(tokens)-1)
        i = aux
    
    return commands.getTokenInfo(tokens[i].lower())

def formatToken(coin):
    print("[BOT] CHANGING STATUS TO {}".format(coin['symbol']))

    token_id = currency.getId(coin)
    token = currency.getTokenInfo(coin)
    usd = currency.getQuote(token, token_id)
    dailyChange = float(token['data'][token_id]['quote']['USD']['percent_change_24h'])

    return {
        'symbol': coin['symbol'],
        'dailyChange': dailyChange,
        'quote': currency.usdToBrl(usd)
    }

async def statusManager(clientObj):
    arrow = ""
    status = ""

    if clientObj['formatedToken']['dailyChange'] > 0:
        arrow = "↗️"
    else:
        arrow = "↘️"

    if clientObj['state'] == 0:
        status = "{} R$ {:.2f}".format(clientObj['formatedToken']['symbol'], clientObj['formatedToken']['quote'])
        clientObj['state'] = 1
    else:
        status = "{} {} {:.2f}%".format(clientObj['formatedToken']['symbol'], arrow, clientObj['formatedToken']['dailyChange'])
        clientObj['state'] = 0
    
    print("[BOT] CHANGING STATUS VIEW TO {} STATE", clientObj['state'])
    print(clientObj)
    await commands.changeStatus(clientObj['client'], status)

def statusInterval(client):
    try:
        global statusTimer

        if statusTimer is not None:
            statusTimer.cancel()

        client = {
            'client': client,
            'formatedToken': formatToken(getCoin()),
            'state': 0
        }

        statusTimer = Timer(interval=120, first_immediately=True, client=client, callback=statusManager)
    except Exception as e:
        print("[BOT] ERRO AO INICIAR O TIMER DE MUDANÇA DE STATUS: {}".format(e))



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