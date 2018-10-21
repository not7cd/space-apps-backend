import json
import pandas
import glob

from collections import defaultdict
from dateutil import parser

path = "A-350"


def parse_date(date):
    return parser.parse(date).date()


def is_date_not_full(date):
    return "?" in date or len(date.split(" ")) != 3


def parse_to_datetable(filename):
    with open(filename) as f:
        print("Parsing " + filename)
        data = pandas.read_fwf(f)
        data = data.drop(data[data["Launch_Date"].map(is_date_not_full)].index)
        data["Launch_Date"] = data["Launch_Date"].apply(parse_date)
        return data

def parse_to_csv(filename):
    datatable = parse_to_datetable(filename)
    datatable.to_csv("parsed/" + filename.split("/")[-1] + ".csv", index=False)

def get_all_launches():
    all_launches = []
    for file in glob.glob("suborbital/*"):
        data = parse_to_datetable(file)
        launches = data.to_dict('records')
        all_launches.extend(launches)
    return all_launches

def get_starts_per_year():
    all_launches = get_all_launches()
    starts_per_year = defaultdict(lambda: 0)
    for launch in all_launches:
        year = launch['Launch_Date'].year
        starts_per_year[str(year)] += 1
    return starts_per_year

def save_suborbital_to_json():
    with open('suborbital.json', 'w') as f_out:
        d = dict(get_starts_per_year())
        json.dump(d, f_out)
