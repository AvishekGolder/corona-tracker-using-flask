from flask import Flask, render_template, request, request_started 
import requests

app = Flask(__name__)

@app.route("/")
def home():

    data = requests.get("https://disease.sh/v2/countries/bangladesh")
    data_pass = data.json()
    return render_template("index.html", data = data_pass)

if __name__ == "__main__":
    app.run()