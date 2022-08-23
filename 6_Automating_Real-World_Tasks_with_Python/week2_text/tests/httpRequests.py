import requests
print()

response = requests.get('https://www.google.com')
response.raise_for_status()

print(response)
print(response.text[:300])
print(response.ok)
print(response.status_code)
