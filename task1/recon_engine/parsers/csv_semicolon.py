from parsers import register_parser
import csv

def parse(file_path):
    with open(file_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=';')
        return list(reader)

register_parser("csv_semicolon", parse)
