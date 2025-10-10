from flask import Flask, jsonify, render_template, request
import requests
from datetime import datetime

app = Flask(__name__)

NASA_API_KEY = "SLgpbUa129m9RtNcei9hrRByJ4eVGAzzXVfKj5cg"

# JSON endpoint
@app.route("/apod", methods=["GET"])
def get_apod():
    date = request.args.get("date")
    
    # Validate date
    if date:
        try:
            date_obj = datetime.strptime(date, "%Y-%m-%d")
            if date_obj < datetime(1995, 6, 16) or date_obj > datetime.today():
                return jsonify({"error": "Date must be between 1995-06-16 and today."})
        except ValueError:
            return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."})
    
    url = "https://api.nasa.gov/planetary/apod"
    params = {"api_key": NASA_API_KEY}
    if date:
        params["date"] = date
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        result = {
            "title": data.get("title"),
            "date": data.get("date"),
            "explanation": data.get("explanation"),
            "url": data.get("url"),
            "hdurl": data.get("hdurl"),
            "media_type": data.get("media_type"),
            "copyright": data.get("copyright", "Public Domain")
        }
        return jsonify(result)
    else:
        return jsonify({"error": "Failed to fetch APOD data"}), response.status_code

# Front-end route
@app.route("/", methods=["GET"])
def home():
    date = request.args.get("date")
    
    # Validate date
    error_message = None
    if date:
        try:
            date_obj = datetime.strptime(date, "%Y-%m-%d")
            if date_obj < datetime(1995, 6, 16) or date_obj > datetime.today():
                error_message = "Date must be between 1995-06-16 and today."
                date = None
        except ValueError:
            error_message = "Invalid date format. Use YYYY-MM-DD."
            date = None
    
    url = "https://api.nasa.gov/planetary/apod"
    params = {"api_key": NASA_API_KEY}
    if date:
        params["date"] = date
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return render_template("index.html", apod=data, selected_date=date or "", error_message=error_message)
    else:
        error_message = "Failed to fetch APOD data."
        return render_template("index.html", apod=None, selected_date=date or "", error_message=error_message)

if __name__ == "__main__":
    app.run(debug=True)
