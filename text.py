import requests

HEADERS = {
    'Authorization': 'Token 3b5c3ed6d6799a0909c3b1c5b2a58a929bd67af1'
}

R = requests.get(
    'http://192.168.0.189:8080/api/projects/', 
    headers=HEADERS
)

print(R.json()['results'][1])

