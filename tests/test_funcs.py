from funcs import (
    get_data,
    filter_by_transactions_type,
    filter_by_presence_of_key_from,
    sort_by_transactions_date,
    get_latest_transactions,
    parse_date_transaction,
    parse_description_transaction,
    parse_property,
    parce_amount,
    parce_currency,
    get_info_about_transaction
)


def test_get_data(response):
    assert get_data('https://reqres.in/api/users/2') == response
    assert get_data('https://qres.in/api/usrs/2') == []


def test_filter_by_transactions_type(
        transaction_list,
        executed_transaction_list):
    assert filter_by_transactions_type(transaction_list, 'EXECUTED') == executed_transaction_list
    assert filter_by_transactions_type([{}], 'EXECUTED') == []
    assert filter_by_transactions_type([], 'EXECUTED') == []
    assert filter_by_transactions_type(transaction_list, 'test') == []


def test_filter_by_presence_of_key_from(transaction_list, transaction_list_with_from):
    assert filter_by_presence_of_key_from(transaction_list, 'from') == transaction_list_with_from
    assert filter_by_presence_of_key_from(transaction_list, 'test') == []
    assert filter_by_presence_of_key_from([], 'from') == []


def test_sort_by_transactions_date(transaction_list, transactions_sorted_by_date):
    assert sort_by_transactions_date(transaction_list) == transactions_sorted_by_date
    assert sort_by_transactions_date([{}]) == []


def test_get_latest_transaction(transaction_list):
    assert get_latest_transactions(3, transaction_list) == transaction_list
    assert get_latest_transactions(5, transaction_list) == transaction_list
    assert len(get_latest_transactions(1, transaction_list)) == 1
    assert get_latest_transactions(-1, transaction_list) == []


def test_parse_data_transaction(transaction, transaction_without_keys):
    assert parse_date_transaction(transaction) == '03.07.2019'
    assert parse_date_transaction(transaction_without_keys) is None
    assert parse_date_transaction({}) is None


def test_parse_description_transaction(transaction, transaction_without_keys):
    assert parse_description_transaction(transaction) == 'Перевод организации'
    assert parse_description_transaction(transaction_without_keys) is None
    assert parse_description_transaction({}) is None


def test_parse_property(transaction):
    assert parse_property(transaction, 'test') == 'Данные отсутствуют'
    assert parse_property(transaction, "to") == 'Счет **5560'
    assert parse_property(transaction, 'from') == 'MasterCard 7158 30** **** 6758'


def test_parse_amount(transaction, transaction_without_keys):
    assert parce_amount(transaction) == '8221.37'
    assert parce_amount(transaction_without_keys) is None
    assert parce_amount({}) is None


def test_parse_currency(transaction, transaction_without_keys):
    assert parce_currency(transaction) == 'USD'
    assert parce_currency(transaction_without_keys) is None
    assert parce_currency({}) is None


def test_get_info_about_transaction(transaction, result_1, result_2):
    assert get_info_about_transaction(transaction) == result_1
    assert get_info_about_transaction({}) == result_2
