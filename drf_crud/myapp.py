import requests
import json

URL = "http://127.0.0.1:8000/stuapi/"

def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
        
    r = requests.get(URL, data = json_data)  # Make a GET request
    
    data = r.json()                            # Parse the JSON data
    
    print(data)
    
get_data() 