import launch_api
from flask import Flask, json
from flask_caching import Cache

import stats

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

@app.route("/<path:subpath>")
def proxy_api(subpath):
    return launch_api.pass_request(subpath)


@app.route("/stats")
@cache.cached(timeout=86400) # cache for a day TODO: precalculate data & store in DB
def starts_per_year():
    starts = stats.get_starts_per_year()
    return json.jsonify(starts)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
