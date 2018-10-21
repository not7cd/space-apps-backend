from datetime import datetime

import requests
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
API_URL = "https://launchlibrary.net/1.4/"

CORS(app)


@app.route("/<path:subpath>")
def proxy_api(subpath):
    return requests.get(url=API_URL + subpath).text


@app.route("/statistics")
def stats():
    url = (
        API_URL
        + "launch/1960-01-01/"
        + datetime.now().strftime("%Y-%m-%d")
        + "?limit=2000"
    )
    all = requests.get(url=url).json()
    count = all["count"]
    launches = all["launches"]
    return str(count)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
