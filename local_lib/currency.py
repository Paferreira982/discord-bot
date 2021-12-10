import requests
import json
import os

def usdToBrl(dolar):
  try:
    response = requests.get("http://economia.awesomeapi.com.br/json/last/USD-BRL")
    response = json.loads(response.text)
    return round(float(response['USDBRL']['bid']) * dolar, 2)
  except Exception as e:
    print(e)

def getId(symbol):
  try:
    parameters = {
      'symbol': symbol
    }

    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': os.environ['coin_market_token'],
    }

    response = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/map", headers=headers, params=parameters)
    response = json.loads(response.text)
    return str(response['data'][0]['id'])

  except Exception as e:
    print(e)

def getTokenQuote(currency):
  try:
    parameters = {
      'slug': currency['slug']
    }

    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': os.environ['coin_market_token'],
    }

    token_id = getId(currency['symbol'])
    response = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest", headers=headers, params=parameters)
    response = json.loads(response.text)

    return round(float(response['data'][token_id]['quote']['USD']['price']),2)
  except Exception as e:
    print(e)