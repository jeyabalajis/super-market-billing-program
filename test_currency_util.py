from unittest import TestCase
from common.currency_util import maximum, subtract
from common.currency import Currency


class Test(TestCase):
    def test_maximum(self):
        currency_inr_100 = Currency(100, Currency.INR)
        currency_inr_120 = Currency(120, Currency.INR)
        currency_inr_350 = Currency(350, Currency.INR)

        max_value = maximum([currency_inr_100, currency_inr_350, currency_inr_120])
        assert (
            max_value.value == 350 and
            max_value.currency_code == Currency.INR
        )

    def test_maximum_empty(self):
        max_value = maximum([])
        assert (
            max_value.value == 0 and
            max_value.currency_code == Currency.INR
        )

    def test_subtract(self):
        currency_inr_100 = Currency(100, Currency.INR)
        currency_inr_120 = Currency(120, Currency.INR)

        result = subtract(currency_inr_120, currency_inr_100)

        assert result.value == 20 and result.currency_code == Currency.INR

