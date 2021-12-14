#Author: Pedro Augusto
import requests
import json
import os

###########################
# CONFIGURATION VARIABLES #
###########################

headers = {
  'Accepts': 'application/json',
  'X-Riot-Token': os.environ['riot_token'],
}

####################
# RIOT API METHODS #
####################

def getSummonerInfo(name):
    try:
        response = requests.get("https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{}".format(name), headers=headers)
        return json.loads(response.text)
    except Exception as e:
        print(e)

def getSummonerRank(summoner):
    try:
        response = requests.get("https://br1.api.riotgames.com/lol/league/v4/entries/by-summoner/{}".format(summoner['id']), headers=headers)
        return json.loads(response.text)
    except Exception as e:
        print(e)