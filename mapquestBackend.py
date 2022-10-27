import requests
import urllib.parse

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "p0Modq3JoAtVS6BXK5P5CinXWhJNUQwI"

distanceUnits = {
    1 : 'km',
    2 : 'miles'
}

def calculateDirection(orig, dest, distanceUnitId):

    url = main_api + urllib.parse.urlencode({
        "key" : key,
        "from" : orig,
        "to" : dest
    })

    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]


    if json_status == 0:

            directionList = []

            tripDuration = json_data['route']['formattedTime']

            distanceUnit = distanceUnits[distanceUnitId]
            distance = json_data['route']['distance']

            if distanceUnit == 'km':
                distance = round(distance*1.61, 2) # convert data to km
            
            for each in json_data["route"]["legs"][0]["maneuvers"]:
                #print(f"{each['narrative']} ({each['distance']} km)")
                directionList.append(f"{each['narrative']} ({each['distance']} {distanceUnit})")
            
            return tripDuration, distance, distanceUnit, directionList, json_status
    else:
        return None, None, None, None, None, json_status
