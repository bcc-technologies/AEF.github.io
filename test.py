import requests

api_url = "https://barreiro14.pythonanywhere.com"

data = {
    'username': 'Directiva2024',
    'password': 'Barryeslomejor'
}

response = requests.post(api_url, json=data)

print(response.json())