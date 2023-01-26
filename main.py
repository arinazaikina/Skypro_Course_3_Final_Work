import os
from funcs import (
    load_data,
    filter_by_transactions_type,
    sort_by_transactions_date,
    get_latest_transactions,
    print_info
)

PATH_TO_JSON_FILE = os.path.join('operations.json')


def main():
    data = load_data(path=PATH_TO_JSON_FILE)
    filtered_data = filter_by_transactions_type(transactions_data=data, transactions_type='EXECUTED')
    sorted_by_date = sort_by_transactions_date(transactions_data=filtered_data)
    last_transactions = get_latest_transactions(amount_latest_operations=5, transactions_data=sorted_by_date)

    for transaction in last_transactions:
        print('*' * 50)
        print_info(transaction_data=transaction)
    print('*' * 50)


if __name__ == '__main__':
    main()
