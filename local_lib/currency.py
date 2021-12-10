import requests
import json
import os

def usdToBrl(dolar):
  try:
    response = requests.get("http://economia.awesomeapi.com.br/json/last/USD-BRL")
    response = json.loads(response.text)
    return round(float(response['USDBRL']['bid'] * dolar), 2)
  except Exception as e:
    print(e)

def test():
  try:
    parameters = {
      'slug': 'bombcrypto'
    }

    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': os.environ['coin_market_token'],
    }

    response = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest", headers=headers, params=parameters)
    response = json.loads(response.text)
    return round(float(response['data'][]),2)

  except Exception as e:
    print(e)