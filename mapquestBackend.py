import requests # Library for sending HTTP requests
import urllib.parse # Combines URL components into a URL string

main_api = "https://www.mapquestapi.com/directions/v2/route?" # API Resource
key = "p0Modq3JoAtVS6BXK5P5CinXWhJNUQwI" # API Key


# Distance Unit Mapping (metric (km) or miles)
distanceUnits = {
    1 : 'km',
    2 : 'miles'
}


# Helper function that calculates the ff:
#   - Distance (km or miles)
#   - Trip Duration
#   - Direction Descriptions with corresponding Distance (km or miles)
def calculateDirection(orig, dest, distanceUnitId):

    # Combines the API resource with given parameters as a URI string
    url = main_api + urllib.parse.urlencode({
        "key" : key,
        "from" : orig,
        "to" : dest
    })

    json_data = requests.get(url).json() # Sends HTTP requests to the API resource with parameters
    json_status = json_data["info"]["statuscode"] # Retrieval of JSON status code


    if json_status == 0: # Successful

            # Containter of tuples that contains the description, distance, and unit
            directionList = [] 
            
            # Retrieval of Trip Duration from the JSON Data returned
            tripDuration = json_data['route']['formattedTime']

            # Declaration of the distance unit based on the the provided input (using distanceUnitsdict)
            distanceUnit = distanceUnits[distanceUnitId]

            # Retrieval of Distance from the JSON Data returned
            distance = json_data['route']['distance']

            # Conversion process
            # Ignore if 'miles' which is the default
            if distanceUnit == 'km': 
                distance = convertMilestoKm(distance) # Converts miles to km
            

            # Iterate through the returned directions
            # Add the corresponding direction, distance, and distance unit as a tuple to directionList
            for each in json_data["route"]["legs"][0]["maneuvers"]:
                #print(f"{each['narrative']} ({each['distance']} km)")
                if distanceUnit == 'km': # Converts each distance to km if distanceUnit declared is km
                    each['distance'] = convertMilestoKm(each['distance'])
                directionList.append((each['narrative'], each['distance'], distanceUnit))
            
            # Return all the necessary data to the call
            return tripDuration, distance, distanceUnit, directionList, json_status
    else:
        # Return None for tripDuration, distance, distanceunit, and directionList if there there are errors
        # Return the JSON status code to identify what the error to be displayed
        return None, None, None, None, json_status


# Helper function that converts miles to km
def convertMilestoKm(miles):
    return round(miles*1.61, 2)
