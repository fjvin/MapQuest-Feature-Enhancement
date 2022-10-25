import requests
import urllib.parse

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "p0Modq3JoAtVS6BXK5P5CinXWhJNUQwI"

while True:
    orig = input("Starting Location: ")
    dest = input("Destination: ")
    url = main_api + urllib.parse.urlencode({
        "key" : key,
        "from" : orig,
        "to" : dest
    })

    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    print(f"URL: {url}")

    if json_status == 0:
        print(f"API Status: {json_status} = A successfull route call.\n")