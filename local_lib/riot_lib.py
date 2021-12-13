#Author: Pedro Augusto
import requests
import json
import os

headers = {
  'Accepts': 'application/json',
  'X-Riot-Token': 'RGAPI-a8de1b1d-f164-4bb1-896f-faa5a53fda24',
}

def getSummonerInfo(name):
    response = requests.get("https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{}".format(name), headers=headers)
    return json.loads(response.text)

def getSummonerRank(summoner):
    response = requests.get("https://br1.api.riotgames.com/lol/league/v4/entries/by-summoner/{}".format(summoner['id']), headers=headers)
    return json.loads(response.text)