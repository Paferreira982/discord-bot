#Author: Pedro Augusto
#Lib currency: Biblioteca que guarda todas as funções relacionadas a tokens e moedas.
import requests
import json
import os

#Cabeçalho utilizado para acesso à API do coinmarketcap
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': os.environ['coin_market_token'],
}

#Função responsável por retornar a conversão de Dolar para BRL em tempo real.
def usdToBrl(dolar):
  try:
    response = requests.get("http://economia.awesomeapi.com.br/json/last/USD-BRL")
    response = json.loads(response.text)
    return float(response['USDBRL']['bid']) * dolar
  except Exception as e:
    print(e)

#Função responsável por obter o ID de um token da API do coinmarketcap
def getId(token):
  try:
    parameters = {
      'symbol': token['symbol']
    }

    response = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/map", headers=headers, params=parameters)
    response = json.loads(response.text)
    
    for data in response['data']:
      if data['slug'] == token['slug']:
        return str(data['id'])
        
    return str(response['data'][0]['id'])

  except Exception as e:
    print(e)

def getTokenInfo(token):
  try:
    parameters = {
      'slug': token['slug']
    }

    response = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest", headers=headers, params=parameters)
    response = json.loads(response.text)

    return response
  except Exception as e:
    print(e)

#Função responsável por obter valor em dolar de um token.
def getTokenQuote(token):
  try:
    response = getTokenInfo(token)
    token_id = getId(token)

    return float(response['data'][token_id]['quote']['USD']['price'])
  except Exception as e:
    print(e)

def getQuote(token, token_id):
  try:
    return float(token['data'][token_id]['quote']['USD']['price'])
  except Exception as e:
    print(e)