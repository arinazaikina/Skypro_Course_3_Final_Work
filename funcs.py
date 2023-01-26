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

print(load_data(path=PATH_TO_JSON_FILE))