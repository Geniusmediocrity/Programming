import requests

import json


def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    with open("text.json", "a") as f:
        f.write(text)
    

response = requests.get("http://api.open-notify.org/astros.json")
jprint(response.json())