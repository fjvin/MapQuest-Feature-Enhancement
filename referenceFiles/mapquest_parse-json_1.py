import requests
import urllib.parse

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Tokyo, Japan"
dest = "Kawaguchi, Japan"
key = "p0Modq3JoAtVS6BXK5P5CinXWhJNUQwI"

url = main_api + urllib.parse.urlencode({
    "key" : key,
    "from" : orig,
    "to" : dest
})

print(f"Formatted URL with variables included: {url}")

json_data = requests.get(url).json()
print(json_data)