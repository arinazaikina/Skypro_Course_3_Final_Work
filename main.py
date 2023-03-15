import warnings
from data.link_to_data import url
from funcs import (
    get_data,
    filter_by_transactions_type,
    filter_by_presence_of_key_from,
    sort_by_transactions_date,
    get_latest_transactions,
    get_info_about_transaction
)

IGNORE_INCOMPLETE_TRANSACTIONS = False


def main() -> None:
    """
    Displays a list of the last 5 completed transactions
    If IGNORE_INCOMPLETE_TRANSACTIONS == False, those transactions are displayed
    that have data from where it was made. Otherwise, filtering by the presence
    of the "from" key is not applied.
    """
    warnings.filterwarnings('ignore', message='Unverified HTTPS request')
    data = get_data(url=url)
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
        print(get_info_about_transaction(transaction_data=transaction))
    print('*' * 50)


if __name__ == '__main__':
    main()
