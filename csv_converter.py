import os

import pandas
import glob

from dateutil import parser

path = "A-350"


def parse_date(date):
    return parser.parse(date).date()


def is_date_not_full(date):
    return "?" in date or len(date.split(" ")) != 3


def parse_to_csv(filename):
    with open(filename) as f:
        print("Parsing " + filename)
        data = pandas.read_fwf(f)
        data = data.drop(data[data["Launch_Date"].map(is_date_not_full)].index)
        data["Launch_Date"] = data["Launch_Date"].apply(parse_date)
        data.to_csv("parsed/" + filename.split("/")[-1] + ".csv", index=False)


for file in glob.glob("suborbital/*"):
    parse_to_csv(file)
