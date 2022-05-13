from turtle import title
import requests

endpoint = "http://localhost:8000/api/products/2/update"

data = {
    'title':'Hello world my old friend',
    'price': 129.99
}

get_response = requests.put(endpoint, json=data)

print(get_response.json())