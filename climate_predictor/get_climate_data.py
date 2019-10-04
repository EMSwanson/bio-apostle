import requests

response = requests.get('http://api.open-notify.org')
print(response.text)
print(response.status_code)
print(response.json())
