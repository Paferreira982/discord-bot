# Author: PEDRO AUGUSTO
# Github: https://github.com/Paferreira982
# Description: Lib with methos to obtain data from riot games API.

import requests
import json
import os

###########################
# CONFIGURATION VARIABLES #
###########################

# HEADERS OF RIOT GAMES API.
headers = {
  'Accepts': 'application/json',
  'X-Riot-Token': os.environ['riot_token'],
}

####################
# RIOT API METHODS #
####################

# RETURNS THE SUMMONERS INFO BY NAME.
def getSummonerInfo(name):
    try:
        response = requests.get("https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{}".format(name), headers=headers)
        return json.loads(response.text)
    except Exception as e:
        print(e)

# RETURNS THE SUMMONERS RANK.
def getSummonerRank(summoner):
    try:
        response = requests.get("https://br1.api.riotgames.com/lol/league/v4/entries/by-summoner/{}".format(summoner['id']), headers=headers)
        return json.loads(response.text)
    except Exception as e:
        print(e)