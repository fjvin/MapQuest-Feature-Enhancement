import requests
import urllib.parse

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "p0Modq3JoAtVS6BXK5P5CinXWhJNUQwI"

while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break

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
        print("="*30)
        print(f"Directions from {orig} to {dest}")
        print(f"Trip Duration: {json_data['route']['formattedTime']}")
        print(f"Kilometers: {round(json_data['route']['distance']*1.61, 2)}")
        print(f"Fuel Used (Ltr): {round(json_data['route']['fuelUsed']*3.78, 2)}")
        print("="*30)
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print(f"{each['narrative']} ({each['distance']} km)")
        print("="*30)