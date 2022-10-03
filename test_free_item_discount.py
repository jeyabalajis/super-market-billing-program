from unittest import TestCase

from common.currency import Currency
from common.price_per_unit import PricePerUnit
from common.unit_of_measure import UnitOfMeasure
from discount.free_item_discount import FreeItemDiscount


class TestFreeItemDiscount(TestCase):
    def test_calculate_discount_amount_more_than_minimum(self):
        quantity_13_kg = UnitOfMeasure(13, UnitOfMeasure.KILO)
        price_50_inr_per_kg = PricePerUnit(Currency(50.0, Currency.INR), UnitOfMeasure(1, UnitOfMeasure.KILO))
        free_item_discount = FreeItemDiscount(
            minimum_purchase_quantity=UnitOfMeasure(3, UnitOfMeasure.KILO),
            free_quantity=UnitOfMeasure(1, UnitOfMeasure.KILO)
        )

        # on 13 kg, there are three chunks of 4 kgs. for each 4 kg, 1kg is free
        # so, on 13 kg, the priced unit_of_measure would be only 10 kg.
        # total discount amount would be (13-10)* 50 = 3*50 = 150
        discount_amount = free_item_discount.calculate_discount_amount(
            quantity_13_kg,
            price_50_inr_per_kg
        )
        assert discount_amount.value == 150.0 and discount_amount.currency_code == Currency.INR

    def test_calculate_discount_less_than_minimum(self):
        quantity_3_kg = UnitOfMeasure(3, UnitOfMeasure.KILO)
        price_50_inr_per_kg = PricePerUnit(Currency(50.0, Currency.INR), UnitOfMeasure(1, UnitOfMeasure.KILO))
        free_item_discount = FreeItemDiscount(
            minimum_purchase_quantity=UnitOfMeasure(3, UnitOfMeasure.KILO),
            free_quantity=UnitOfMeasure(1, UnitOfMeasure.KILO)
        )

        # on purchase of 3 kg, 1 kg free.
        # Since the purchase unit_of_measure is 3 kg, no discount
        discount_amount = free_item_discount.calculate_discount_amount(
            quantity_3_kg,
            price_50_inr_per_kg
        )

        assert discount_amount.value == 0.0 and discount_amount.currency_code == Currency.INR

    def test_calculate_discount_equal_to_minimum(self):
        quantity_4_kg = UnitOfMeasure(4, UnitOfMeasure.KILO)
        price_50_per_kg = PricePerUnit(Currency(50.0, Currency.INR), UnitOfMeasure(1, UnitOfMeasure.KILO))
        free_item_discount = FreeItemDiscount(
            minimum_purchase_quantity=UnitOfMeasure(3, UnitOfMeasure.KILO),
            free_quantity=UnitOfMeasure(1, UnitOfMeasure.KILO)
        )

        # on purchase of 3 kg, 1 kg free.
        # on 4 kg, 1 kg is free, hence discount amount is 1 kg * 50 inr per kg = 50
        discount_amount = free_item_discount.calculate_discount_amount(
            quantity_4_kg,
            price_50_per_kg
        )
        assert discount_amount.value == 50.0 and discount_amount.currency_code == Currency.INR
