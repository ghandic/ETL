import argparse

def get_cli():
    parser = argparse.ArgumentParser(description='ETL tool for flattening people')
    parser.add_argument('input', type=str, help='Input file to run through ETL pipeline')
    parser.add_argument('--output', default="flat_people.csv", help='Output file location for the CSV producedby the ETL pipeline')
    args = parser.parse_args()
    return args