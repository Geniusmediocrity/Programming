import requests


get_r = requests.get(url="http://firstctf.ru:8001/monster#/default/set_cookie_cookie_post")
print(get_r.text)
