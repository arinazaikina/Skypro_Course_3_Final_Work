import json
from datetime import datetime
from typing import List, Dict


def load_data(path: str) -> List[Dict[str, str]]:
    """
    Loads data from a json-file
    """
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def filter_by_transactions_type(transactions_data: List[Dict[str, str]], transactions_type: str) -> List[Dict[str, str]]:
    """
    Filters data by operation type
    """
    filtered_data = []
    for transaction in transactions_data:
        if transaction.get('state') == transactions_type:
            filtered_data.append(transaction)
    return filtered_data


def filter_by_presence_of_key_from(transactions_data: List[Dict[str, str]], key:str) -> List[Dict[str, str]]:
    """
    Filters data by the presence of the "from" key
    """
    filtered_data = []
    for transaction in transactions_data:
        if key in transaction:
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
    Returns latest transactions
    """
    return transactions_data[:amount_latest_operations]


def parse_date_transaction(transaction_data: Dict[str, str]) -> str:
    """
    Returns the formatted transaction date
    """
    raw_date = transaction_data.get('date')
    date_time_obj = datetime.strptime(raw_date, '%Y-%m-%dT%H:%M:%S.%f')
    formatted_data = f'{date_time_obj.day}.{date_time_obj.month}.{date_time_obj.year}'
    return formatted_data


def parse_description_transaction(transaction_data: Dict[str, str]) -> str:
    """
    Returns a description of the transaction
    """
    description = transaction_data.get('description')
    return description


def parse_property(transaction_data: Dict[str, str], direction: str) -> str:
    """
    Returns formatted props
    """
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
    """
    Returns the transaction amount
    """
    operation_amount = transaction_data.get('operationAmount')
    amount = operation_amount.get('amount')
    return amount


def parce_currency(transaction_data: Dict[str, str]) -> str:
    """
    Returns the transaction currency
    """
    operation_amount = transaction_data.get('operationAmount')
    amount = operation_amount.get('currency').get('name')
    return amount


def print_info(transaction_data: Dict[str, str]) -> None:
    """
    Displays information about the transaction
    """
    result = f'{parse_date_transaction(transaction_data)} {parse_description_transaction(transaction_data)}\n' \
             f'{parse_property(transaction_data, direction="from")} -> {parse_property(transaction_data, direction="to")}\n' \
             f'{parce_amount(transaction_data)} {parce_currency(transaction_data)}'
    print(result)
