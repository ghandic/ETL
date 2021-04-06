from etl import from_json, flatten_people, to_csv

import typer
from pick import pick

def main(input: str):

    title = 'Please pick your output file name:'
    options = ['example.csv', "flat_people.csv"]
    option, _ = pick(options, title)

    print("Extracting JSON data...")
    people = from_json(input)

    print("Transforming nested people into flat people...")
    flat_people=flatten_people(people)

    print("Loading flattened people into a CSV file...")
    to_csv(flat_people, option)

if __name__ == "__main__":
    typer.run(main)