import requests

headers = {'Authorization': 'Bearer 3bd24931e19d84b62a8a59fb8dc7acdc2388ebde'}

endpoint = "http://localhost:8000/api/products/"

data = {
    'title':'this field is done!!!!', 
    'price': 31.50
}

get_response = requests.post(endpoint, json=data, headers=headers)

print(get_response.json())