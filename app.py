"""
Simple "Hello, World" application using Flask
"""

from flask import Flask, render_template, request
from mbta_helper import *

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def MBTAHelper():
    if request.method == "POST":
        location = str(request.form["location"])
        MBTA_Station, wheelchair = find_stop_near(location)
        if location:
            return render_template("mbta_result.html", location = location, MBTA_Station = MBTA_Station, wheelchair = wheelchair)
        else:
            return render_template('index.html')
    return render_template('index.html')