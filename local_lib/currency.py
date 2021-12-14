import requests
import json
import os

###########################
# CONFIGURATION VARIABLES #
###########################

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': os.environ['coin_market_token'],
}

######################
# AWSOME API METHODS #
###################### 

def usdToBrl(dolar):
  try:
    response = requests.get("http://economia.awesomeapi.com.br/json/last/USD-BRL")
    response = json.loads(response.text)
    return float(response['USDBRL']['bid']) * dolar
  except Exception as e:
    print(e)

###############################
# COIN MARKET CAP API METHODS #
############################### 

def getId(coin):
  try:
    parameters = {
      'symbol': coin['symbol']
    }

    response = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/map", headers=headers, params=parameters)
    response = json.loads(response.text)
    
    for data in response['data']:
      if data['slug'] == coin['slug']:
        return str(data['id'])
        
    return str(response['data'][0]['id'])

  except Exception as e:
    print(e)

def getTokenInfo(coin):
  try:
    parameters = {
      'slug': coin['slug']
    }

    response = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest", headers=headers, params=parameters)
    response = json.loads(response.text)

    return response
  except Exception as e:
    print(e)

def getTokenQuote(coin):
  try:
    response = getTokenInfo(coin)
    token_id = getId(coin)

    return float(response['data'][token_id]['quote']['USD']['price'])
  except Exception as e:
    print(e)

def getQuote(token, token_id):
  try:
    return float(token['data'][token_id]['quote']['USD']['price'])
  except Exception as e:
    print(e)