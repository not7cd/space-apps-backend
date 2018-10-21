from flask import jsonify
from flask_caching import Cache
from flask import Flask, json
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
