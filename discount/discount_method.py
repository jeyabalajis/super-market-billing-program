from abc import ABC, abstractmethod

from common.currency import Currency
from common.unit_of_measure import UnitOfMeasure
from common.price_per_unit import PricePerUnit


class DiscountMethod(ABC):
    def __init__(self):
        """abstract base class"""
        pass

    @abstractmethod
    def calculate_discount_amount(self, unit_of_measure: UnitOfMeasure, price_per_unit: PricePerUnit) -> Currency:
        pass
