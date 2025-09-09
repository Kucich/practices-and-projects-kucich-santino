import requests

url = "https://api.adviceslip.com/advice"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Consejo del día:")
    print(data["slip"]["advice"])
else:
    print("Error:", response.status_code)
