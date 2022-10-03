from abc import ABC, abstractmethod

from common.currency import Currency
from order.item import Item


class DiscountStrategy(ABC):
    def __init__(self):
        """
        abstract base class
        """
        pass

    @abstractmethod
    def calculate_discount_amount(self, item: Item) -> Currency:
        pass
