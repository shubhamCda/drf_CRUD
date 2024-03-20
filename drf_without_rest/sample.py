import json
import requests

BASE_URL = "http://127.0.0.1:8000/"
ENDPOINT = "api/"

resp = requests.get("https://catfact.ninja/fact/")
p_data = resp.json()
print(p_data)
