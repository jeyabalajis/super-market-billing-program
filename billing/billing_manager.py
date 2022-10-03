from typing import List

from billing.bill_item import BillItem
from discount.discount_strategy import DiscountStrategy
from order.order import Order
from common.amount_calculator import AmountCalculator
from common.currency_util import subtract


class BillingManager:
    def __init__(self, order: Order, discount_strategy: DiscountStrategy):
        self.order = order
        self.discount_strategy = discount_strategy

    def compute_bill(self) -> List[BillItem]:

        bill_items = []
        for item in self.order.items:
            discount_amount = self.discount_strategy.calculate_discount_amount(item)
            item_amount = AmountCalculator(item.quantity, item.store_product.price_per_unit).calculate_amount()
            bill_item = BillItem(
                item=item,
                item_amount=item_amount,
                billed_amount=subtract(item_amount, discount_amount),
                discount_amount=discount_amount
            )
            bill_items.append(bill_item)

        return bill_items
