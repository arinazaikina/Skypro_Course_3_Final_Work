import json
import os
from typing import List, Dict

PATH_TO_JSON_FILE = os.path.join('operations.json')

def load_data(path: str) -> List[Dict[str, str]]:
    """
    Loads data from a json-file
    """
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def filter_by_operation_type(operations_data: List[Dict[str, str]], operation_type: str) -> List[Dict[str, str]]:
    """
    Filters data by operation type
    """
    filtered_data = []
    for operation in operations_data:
        if operation.get('state') == operation_type:
            print(operation['state'])
            filtered_data.append(operation)
    return filtered_data

# data = load_data(path=PATH_TO_JSON_FILE)
# print(data)
# filtered = filter_by_operation_type(operations_data=data, operation_type='EXECUTED')
# print(filtered)