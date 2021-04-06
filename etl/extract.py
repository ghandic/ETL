import json


def from_json(file:str)->dict:
    with open(file, "r") as file:
        return json.load(file)

