from common.currency import Currency
from order.item import Item


class BillItem:
    def __init__(self, *, item: Item, item_amount: Currency, billed_amount: Currency, discount_amount: Currency):
        self.item = item
        self.item_amount = item_amount
        self.billed_amount = billed_amount
        self.discount_amount = discount_amount
