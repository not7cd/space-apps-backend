import requests
from flask import Flask

app = Flask(__name__)
API_URL = "https://launchlibrary.net/1.4/"

@app.route("/<path:subpath>")
def proxy_api(subpath):
    return requests.get(url=API_URL + subpath).text

if __name__ == '__main__':
    app.run(debug=True)