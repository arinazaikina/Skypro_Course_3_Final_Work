import json
import os
from typing import List, Dict
from datetime import datetime

PATH_TO_JSON_FILE = os.path.join('operations.json')


def load_data(path: str) -> List[Dict[str, str]]:
    """
    Loads data from a json-file
    """
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def filter_by_transactions_type(transactions_data: List[Dict[str, str]], transactions_type: str) -> List[
    Dict[str, str]]:
    """
    Filters data by operation type
    """
    filtered_data = []
    for transaction in transactions_data:
        if transaction.get('state') == transactions_type:
            filtered_data.append(transaction)
    return filtered_data


def sort_by_transactions_date(transactions_data: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """
    Sort transactions by date
    """
    sorted_data_by_date = sorted(transactions_data, key=lambda x: x['date'], reverse=True)
    return sorted_data_by_date


def get_latest_transactions(amount_latest_operations: int,
                            transactions_data: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """
    Get latest transactions
    """
    return transactions_data[:amount_latest_operations]


data = load_data(path=PATH_TO_JSON_FILE)
filtered_data = filter_by_transactions_type(transactions_data=data, transactions_type='EXECUTED')
sorted_by_date = sort_by_transactions_date(transactions_data=filtered_data)
last_transactions = get_latest_transactions(amount_latest_operations=5, transactions_data=sorted_by_date)


def parse_date_transaction(transaction_data: Dict[str, str]) -> str:
    raw_date = transaction_data.get('date')
    date_time_obj = datetime.strptime(raw_date, '%Y-%m-%dT%H:%M:%S.%f')
    formatted_data = f'{date_time_obj.day}.{date_time_obj.month}.{date_time_obj.year}'
    return formatted_data


def parse_description_transaction(transaction_data: Dict[str, str]) -> str:
    description = transaction_data.get('description')
    return description


def parse_property(transaction_data: Dict[str, str], direction: str) -> str:
    raw_sender = transaction_data.get(direction)
    if raw_sender is None:
        return 'Данные об отправителе отсутствуют'
    if raw_sender.split()[0] == 'Счет':
        return f'{raw_sender.split()[0]} ' + '**' + f'{raw_sender.split()[1][-4:]}'
    card_number = ''
    name_card = ''
    for symbol in raw_sender:
        if symbol.isdigit():
            card_number += symbol
        else:
            name_card += symbol
    card_number_hide = f'{card_number[:4]} ' + f'{card_number[4:6]}' + '** **** ' + f'{card_number[-4:]}'
    return f'{name_card} {card_number_hide}'


def parce_amount(transaction_data: Dict[str, str]):
    operation_amount = transaction_data.get('operationAmount')
    amount = operation_amount.get('amount')
    return amount


def parce_currency(transaction_data: Dict[str, str]) -> str:
    operation_amount = transaction_data.get('operationAmount')
    amount = operation_amount.get('currency').get('name')
    return amount


def print_info(transaction_data: Dict[str, str]) -> None:
    result = f'{parse_date_transaction(transaction_data)} {parse_description_transaction(transaction_data)}\n' \
             f'{parse_property(transaction_data, direction="from")} -> {parse_property(transaction_data, direction="to")}\n' \
             f'{parce_amount(transaction_data)} {parce_currency(transaction_data)}'
    print(result)

