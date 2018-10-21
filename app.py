import json
import os

from flask import jsonify
from flask_caching import Cache
from flask import Flask
from flask_cors import CORS

import stats
import launch_api

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
CORS(app)


@app.route("/<path:subpath>")
def proxy_api(subpath):
    return jsonify(launch_api.pass_request(subpath))


@app.route("/stats")
@cache.cached(timeout=86400) # cache for a day TODO: precalculate data & store in DB
def starts_per_year():
    starts = stats.get_starts_per_year()
    return jsonify(starts)


@app.route("/stats/suborbital")
@cache.cached(timeout=86400) # cache for a day
def suborbital_stats():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "suborbital.json")
    data = json.load(open(json_url))
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
