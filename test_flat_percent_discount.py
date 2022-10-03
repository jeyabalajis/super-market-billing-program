from unittest import TestCase

from common.currency import Currency
from common.discount_percent import DiscountPercent
from common.price_per_unit import PricePerUnit
from discount.flat_percent_discount import FlatPercentageDiscount
from common.unit_of_measure import UnitOfMeasure


class TestFlatPercentDiscount(TestCase):
    def test_calculate_discount_amount(self):
        quantity_10_kg = UnitOfMeasure(10, UnitOfMeasure.KILO)
        price_50_inr_per_kg = PricePerUnit(Currency(50.0, Currency.INR), UnitOfMeasure(1, UnitOfMeasure.KILO))
        discount_40_percent = DiscountPercent(40.0)
        flat_40_percent_discount = FlatPercentageDiscount(discount_40_percent)

        discount_amount = flat_40_percent_discount.calculate_discount_amount(
            quantity_10_kg,
            price_50_inr_per_kg
        )

        assert discount_amount.value == 200.0 and discount_amount.currency_code == Currency.INR

