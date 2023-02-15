import json
import csv

def flatten_json(nested_json, flat_json={}, prefix=''):
    """Recursively flattens a nested JSON object"""
    for key, value in nested_json.items():
        if isinstance(value, dict):
            flatten_json(value, flat_json, prefix + key + '_')
        else:
            flat_json[prefix + key] = value
    return flat_json

def json_to_csv(json_file, csv_file):
    """Converts a JSON file to a CSV file"""
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    flat_data = []
    for item in data:
        flat_item = flatten_json(item)
        flat_data.append(flat_item)
    
    headers = set()
    for item in flat_data:
        for key in item.keys():
            headers.add(key)
    
    with open(csv_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=sorted(headers))
        writer.writeheader()
        for item in flat_data:
            writer.writerow(item)

json_file = 'OAPI_applications.json'
csv_file = 'output.csv'
json_to_csv(json_file, csv_file)
