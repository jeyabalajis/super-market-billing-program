from unittest import TestCase

from billing.billing_manager import BillingManager
from discount.max_discount_strategy import MaxDiscountStrategy
from discount.max_or_free_item_discount_strategy import MaxOrFreeItemDiscountStrategy
from order.item import Item
from order.order import Order
from product.category import Category
from product.product import Product
from product.sub_category import SubCategory
from store.store import Store
from store.store_product import StoreProduct
from common.currency import Currency
from common.discount_percent import DiscountPercent
from common.price_per_unit import PricePerUnit

from common.unit_of_measure import UnitOfMeasure
from discount.flat_percent_discount import FlatPercentageDiscount
from discount.free_item_discount import FreeItemDiscount


class TestBillingManager(TestCase):
    def test_compute_bill(self):
        category_produce = Category("Produce", FlatPercentageDiscount(DiscountPercent(10)))
        sub_category_fruits = SubCategory("Fruits", FlatPercentageDiscount(DiscountPercent(18)))

        free_item_discount = FreeItemDiscount(
            minimum_purchase_quantity=UnitOfMeasure(3, UnitOfMeasure.KILO),
            free_quantity=UnitOfMeasure(1, UnitOfMeasure.KILO)
        )

        product_apple = Product(
            "Apple",
            category_produce,
            sub_category_fruits,
            free_item_discount
        )

        product_orange = Product(
            "Orange",
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

        store_1_orange = StoreProduct(
            store_1,
            product_orange,
            PricePerUnit(Currency(80.0, Currency.INR), UnitOfMeasure(1, UnitOfMeasure.KILO))
        )

        order_item_apple = Item(store_1_apple, UnitOfMeasure(6, UnitOfMeasure.KILO))
        order_item_orange = Item(store_1_orange, UnitOfMeasure(2, UnitOfMeasure.KILO))
        order = Order([order_item_apple, order_item_orange])

        max_or_free_item_discount_strategy = MaxOrFreeItemDiscountStrategy()

        assert max_or_free_item_discount_strategy.calculate_discount_amount(order_item_apple).value == 50.0
        assert max_or_free_item_discount_strategy.calculate_discount_amount(order_item_orange).value == 32.0

        max_discount_strategy = MaxDiscountStrategy()
        assert max_discount_strategy.calculate_discount_amount(order_item_apple).value == 54.0

        billing_manager_1 = BillingManager(order, max_or_free_item_discount_strategy)
        bill_items = billing_manager_1.compute_bill()

        total_discount_amount = 0
        total_item_amount = 0
        total_billed_amount = 0
        for bill_item in bill_items:
            name = bill_item.item.store_product.product.name
            item_amount = bill_item.item_amount.value
            discount_amt = bill_item.discount_amount.value
            billed_amt = bill_item.billed_amount.value

            print(f"Item: {name} Amount: {item_amount} Disc: {discount_amt} Billed: {billed_amt}")
                
            total_item_amount += bill_item.item_amount.value
            total_discount_amount += bill_item.discount_amount.value
            total_billed_amount += bill_item.billed_amount.value

        assert total_item_amount == 460.0
        assert total_discount_amount == 82.0
        assert total_billed_amount == 378.00

