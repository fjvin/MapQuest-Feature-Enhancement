from flask import Flask, flash
from flask import request
from flask import render_template
from mapquestBackend import calculateDirection

app = Flask(__name__)
app.secret_key = "wsjlhfgsehjdfgsjadhfgjsakdhfg"


@app.route("/", methods=["POST", "GET"])
def main():
    if request.method == "POST":
        orig = request.form['start']
        dest = request.form['dest']
        distanceUnitId = int(request.form['distanceUnit'])
        
        tripDuration, distance, distanceUnit, directionList, json_status = calculateDirection(orig, dest, distanceUnitId)
        dataPayload = {
            'tripDuration': tripDuration,
            'distance': distance,
            'distanceUnit' : distanceUnit,
            'directionList': directionList,
            'json_status': json_status,
            'orig' : orig,
            'dest' : dest
        }

        if json_status == 0:
            flash('Success', 'success')
            flashWarning = 'success'
            return render_template("index.html", dataPayload=dataPayload, flashWarning=flashWarning, request=request)
        elif json_status == 402:
            message = f"Status Code: {json_status}; Invalid user inputs for one or both locations."
            flash(message, 'warning')
            flashWarning = 'warning'
            return render_template("index.html", dataPayload=dataPayload, flashWarning=flashWarning, request=request)
        elif json_status == 611:
            message = f"Status Code: {json_status}; Missing an entry for one or both locations."
            flash(message, 'warning')
            flashWarning = 'warning'
            return render_template("index.html", dataPayload=dataPayload, flashWarning=flashWarning, request=request)
        else:
            message = f"Status Code: {json_status}; Missing an entry for one or both locations."
            flash(message, 'warning')
            flashWarning = 'warning'
            return render_template("index.html", dataPayload=dataPayload, flashWarning=flashWarning, request=request)
      
    else:
        return render_template("index.html")



if __name__ == "__main__":
    app.run()
