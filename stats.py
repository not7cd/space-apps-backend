from collections import defaultdict
from dateutil import parser

import launch_api


def get_starts_per_year():
    launches = launch_api.get_all_launches()
    starts_per_year = defaultdict(lambda: 0)
    for launch in launches:
        year = parser.parse(launch['net']).year
        starts_per_year[str(year)] += 1
    return starts_per_year


def get_suborbital_starts_per_year():
    launches = launch_api.get_all_launches()
    starts_per_year = defaultdict(lambda: 0)
    for launch in launches:
        year = parser.parse(launch['Launch_date']).year
        starts_per_year[str(year)] += 1
    return starts_per_year