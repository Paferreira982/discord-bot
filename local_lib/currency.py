import requests
import json

def USDToBRL(dolar):
  response = requests.get("http://economia.awesomeapi.com.br/json/last/USD-BRL")
  response = json.loads(response.text)
  return response['USDBRL']['bid'] * dolar