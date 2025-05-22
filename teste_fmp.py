import requests
api_key = "EXJdqaeDxTfNvCKIc73ke4Go05xGV8kn"  # Substitua pela chave da FMP
symbol = "PETR4.SA"
url = f"https://financialmodelingprep.com/api/v3/profile/{symbol}?apikey={api_key}"
response = requests.get(url)
print(response.json())