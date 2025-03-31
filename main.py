import requests

r = requests.get('https://google.com')

print("Status code : " , r.status_code)