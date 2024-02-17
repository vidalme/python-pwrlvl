import requests

API_KEY = 'fca_live_UUaMHrs2GcmfyhNnPCuoP4ccdkRQrhAdZjwIQNQi'
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["BRL","USD","EUR","JPY","CNY"]

def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    except:
        print("Moeda invalida, você pode encontrar a relação de moedas válidas em https://freecurrencyapi.com/docs/currency-list")
        return None

while True:
    base = input("Insira a moeda que deseja converter (X para sair): ").upper()
    if base == "X":
        break
    
    data = convert_currency(base)
    if not data:
        continue  
    del data[base]
    for ticker, value in data.items():
        print(f"{ticker}: {value}")
