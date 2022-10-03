from unittest import TestCase
from common.unit_of_measure import UnitOfMeasure
from common.price_per_unit import PricePerUnit
from common.currency import Currency
from common.amount_calculator import AmountCalculator


class TestAmountCalculator(TestCase):
    def test_calculate_amount(self):
        quantity_10_kg = UnitOfMeasure(10, UnitOfMeasure.KILO)
        price_50_inr_per_kg = PricePerUnit(Currency(50, Currency.INR), UnitOfMeasure(1, UnitOfMeasure.KILO))

        total_amount = AmountCalculator(quantity_10_kg, price_50_inr_per_kg).calculate_amount()

        assert total_amount.value == 500.0 and total_amount.currency_code == Currency.INR

    def test_calculate_amount_float(self):
        quantity_10_kg = UnitOfMeasure(13, UnitOfMeasure.KILO)
        price_50_inr_per_kg = PricePerUnit(Currency(50.5, Currency.INR), UnitOfMeasure(1, UnitOfMeasure.KILO))

        total_amount = AmountCalculator(quantity_10_kg, price_50_inr_per_kg).calculate_amount()

        assert total_amount.value == 656.5 and total_amount.currency_code == Currency.INR
