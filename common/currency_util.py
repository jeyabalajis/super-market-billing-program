from typing import List
from common.currency import Currency


def maximum(currencies: List[Currency]):
    """
    TODO: cross currency conversion handling. Can keep a global currency to exchange mixed currency values into a single currency
    before comparison.
    :param currencies:
    :return:
    """
    if currencies is None or len(currencies) == 0:
        return Currency(0, Currency.INR)

    max_value = Currency(-9999.0, currencies[0].currency_code)

    for currency in currencies:
        if currency.value >= max_value.value:
            max_value = currency

    return max_value


def subtract(currency_1: Currency, currency_2: Currency):
    result_value = currency_1.value - currency_2.value
    return Currency(result_value, currency_1.currency_code)
