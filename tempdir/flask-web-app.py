# Library dependecies
from flask import Flask, flash
from flask import request
from flask import render_template
from mapquestBackend import calculateDirection

# App Initialization
app = Flask(__name__) # Flask app instance
app.secret_key = "wsjlhfgsehjdfgsjadhfgjsakdhfg" # Flask API secret key


@app.route("/", methods=["POST", "GET"]) # Default route with POST and GET methods
def main():
    if request.method == "POST": # If request is POST method
        orig = request.form['start'] # Retrieve the starting location input from the HTML form
        dest = request.form['dest'] # Retrieve the destination input from the HTML form
        distanceUnitId = int(request.form['distanceUnit']) # Retrieve the distance unit input from the HTML form
        
        # Calls the helper function to return the tripDuration, distance, distanceUnit, directionList, and json_status
        # Requires three (3) parameters: Starting Location, Destination, and Distance Unit ID
        tripDuration, distance, distanceUnit, directionList, json_status = calculateDirection(orig, dest, distanceUnitId)
        
        # Encapsulate the results into a dictionary variable
        dataPayload = {
            'tripDuration': tripDuration,
            'distance': distance,
            'distanceUnit' : distanceUnit,
            'directionList': directionList,
            'json_status': json_status,
            'orig' : orig,
            'dest' : dest
        }

        # If JSON data has been returned by the API - Successful
        if json_status == 0:
            flash('Success', 'success') # Return a flash success
            flashWarning = 'success' # flashWarning set to success to change alert colors in HTML
            # Return and render index.html with passed data to display other contents (results)
            # Provide also the request to only display the results when the method is POST
            return render_template("index.html", dataPayload=dataPayload, flashWarning=flashWarning, request=request)
        # If one or both of the input fields are invalid
        elif json_status == 402:
            # Return message and flash warning
            message = f"Status Code: {json_status}; Invalid user inputs for one or both locations."
            flash(message, 'warning')
            flashWarning = 'warning'
            # Return and render index.html with dataPayload containing only None values and json_status
            # Provide also the request to only display the flash message when the method is POST
            return render_template("index.html", dataPayload=dataPayload, flashWarning=flashWarning, request=request)
        # If one or both of the input fields are missing
        elif json_status == 611:
            # Return message and flash warning
            message = f"Status Code: {json_status}; Missing an entry for one or both locations."
            flash(message, 'warning')
            flashWarning = 'warning'
            # Return and render index.html with dataPayload containing only None values and json_status
            # Provide also the request to only display the flash message when the method is POST
            return render_template("index.html", dataPayload=dataPayload, flashWarning=flashWarning, request=request)
        # Other Error
        else:
            # Return message and flash warning
            message = f"For Status Code: {json_status}; Refer to: https://developer.mapquest.com/documentation/directions-api/status-codes"
            flash(message, 'warning')
            flashWarning = 'warning'
            # Return and render index.html with dataPayload containing only None values and json_status
            # Provide also the request to only display the flash message when the method is POST
            return render_template("index.html", dataPayload=dataPayload, flashWarning=flashWarning, request=request)
      
    else: # Return the template with no content results when the method is GET
        return render_template("index.html")


# Execute this codeblock when executed directly, not as an import file
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6060)
