from unittest import TestCase

from common.currency import Currency
from common.discount_percent import DiscountPercent
from common.price_per_unit import PricePerUnit

from common.unit_of_measure import UnitOfMeasure
from discount.flat_percent_discount import FlatPercentageDiscount
from discount.free_item_discount import FreeItemDiscount
from discount.max_discount_strategy import MaxDiscountStrategy
from order.item import Item
from product.category import Category
from product.product import Product
from product.sub_category import SubCategory
from store.store import Store
from store.store_product import StoreProduct


class TestMaxDiscountStrategy(TestCase):
    def test_calculate_discount_amount_free_item_discount(self):
        category_produce = Category("Produce", FlatPercentageDiscount(DiscountPercent(10)))
        sub_category_fruits = SubCategory("Fruits", FlatPercentageDiscount(DiscountPercent(18)))
        product_apple = Product(
            "Apple",
            category_produce,
            sub_category_fruits,
            FreeItemDiscount(
                minimum_purchase_quantity=UnitOfMeasure(3, UnitOfMeasure.KILO),
                free_quantity=UnitOfMeasure(1, UnitOfMeasure.KILO)
            )
        )

        store_1 = Store("1", "local store")
        store_1_apple = StoreProduct(
            store_1,
            product_apple,
            PricePerUnit(Currency(50.0, Currency.INR), UnitOfMeasure(1, UnitOfMeasure.KILO))
        )

        billing_item = Item(store_1_apple, UnitOfMeasure(6, UnitOfMeasure.KILO))

        discount_amount = MaxDiscountStrategy().calculate_discount_amount(billing_item)
        assert discount_amount.value == 54.0 and discount_amount.currency_code == Currency.INR

    def test_calculate_discount_amount_flat_percent_discount(self):
        category_produce = Category("Produce", FlatPercentageDiscount(DiscountPercent(10)))
        sub_category_fruits = SubCategory("Fruits", FlatPercentageDiscount(DiscountPercent(18)))
        product_apple = Product(
            "Apple",
            category_produce,
            sub_category_fruits,
            FlatPercentageDiscount(DiscountPercent(20))
        )

        store_1 = Store("1", "local store")
        store_1_apple = StoreProduct(
            store_1,
            product_apple,
            PricePerUnit(Currency(50.0, Currency.INR), UnitOfMeasure(1, UnitOfMeasure.KILO))
        )

        billing_item = Item(store_1_apple, UnitOfMeasure(6, UnitOfMeasure.KILO))
        discount_amount = MaxDiscountStrategy().calculate_discount_amount(billing_item)
        assert discount_amount.value == 60.0 and discount_amount.currency_code == Currency.INR
