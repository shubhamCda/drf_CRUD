import requests
import json

URL = ""

def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
        
    r = requests.get(url=URL, data = json_data)  # Make a GET request
    
    data = r.json()                            # Parse the JSON data
    
    print(data)
    
get_data() 