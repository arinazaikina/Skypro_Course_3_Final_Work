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
            filtered_data.append(operation)
    return filtered_data


def sort_by_transaction_date(operations_data: List[Dict[str, str]]) -> List[Dict[str, str]]:
    sorted_data_by_date = sorted(operations_data, key=lambda x: x['date'], reverse=True)
    return sorted_data_by_date


def get_latest_transactions(amount_latest_operations: int, operations_data: List[Dict[str, str]]) -> List[
    Dict[str, str]]:
    return operations_data[:amount_latest_operations]

#
# data = load_data(path=PATH_TO_JSON_FILE)
# filtered_data = filter_by_operation_type(operations_data=data, operation_type='EXECUTED')
# sort_data = sort_by_transaction_date(operations_data=filtered_data)
# latest_data = get_latest_transactions(amount_latest_operations=5, operations_data=sort_data)
# for i in latest_data:
#     print(i)
