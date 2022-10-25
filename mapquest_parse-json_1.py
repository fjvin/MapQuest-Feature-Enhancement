import urllib.parse
import requests

main_api = "http://www.mapquestapi.com/directions/v2/route?"
orig = "Rome, Italy"
dest = "Frascati, Italy"
key = "LlTItOn3xixWMpX0pPXKH33FKUwAaPRi"

url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest}) 

json_data = requests.get(url).json()
print(json_data)
