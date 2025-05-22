import requests
api_key = "SUA_CHAVE_AQUI"  # Substitua pela chave da FMP
symbol = "PETR4.SA"
url = f"https://financialmodelingprep.com/api/v3/profile/{symbol}?apikey={api_key}"
response = requests.get(url)
print(response.json())