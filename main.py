import os
from funcs import (
    load_data,
    filter_by_transactions_type,
    filter_by_presence_of_key_from,
    sort_by_transactions_date,
    get_latest_transactions,
    print_info
)


IGNORE_INCOMPLETE_TRANSACTIONS = False
PATH_TO_JSON_FILE = os.path.join('operations.json')


def main() -> None:
    """
    Displays a list of the last 5 completed transactions
    If IGNORE_INCOMPLETE_TRANSACTIONS == False, those transactions are displayed
    that have data from where it was made. Otherwise, filtering by the presence
    of the "from" key is not applied.
    """
    data = load_data(path=PATH_TO_JSON_FILE)
    filtered_data_by_transactions_type = filter_by_transactions_type(
        transactions_data=data,
        transactions_type='EXECUTED'
    )
    if not IGNORE_INCOMPLETE_TRANSACTIONS:
        filtered_data_by_complete_transactions = filter_by_presence_of_key_from(
            transactions_data=filtered_data_by_transactions_type,
            key="from"
        )
        data_before_sorted = filtered_data_by_complete_transactions
    else:
        data_before_sorted = filtered_data_by_transactions_type

    sorted_by_date = sort_by_transactions_date(transactions_data=data_before_sorted)
    last_transactions = get_latest_transactions(amount_latest_operations=5, transactions_data=sorted_by_date)

    for transaction in last_transactions:
        print('*' * 50)
        print_info(transaction_data=transaction)
    print('*' * 50)


if __name__ == '__main__':
    main()
