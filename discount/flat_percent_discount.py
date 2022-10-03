from common.currency import Currency
from discount.discount_method import DiscountMethod
from common.unit_of_measure import UnitOfMeasure
from common.price_per_unit import PricePerUnit
from common.discount_percent import DiscountPercent
from common.amount_calculator import AmountCalculator


class FlatPercentageDiscount(DiscountMethod):
    def __init__(self, discount_percent: DiscountPercent):
        super().__init__()
        self.discount_percent = discount_percent

    def calculate_discount_amount(self, unit_of_measure: UnitOfMeasure, price_per_unit: PricePerUnit) -> Currency:
        super(FlatPercentageDiscount, self).calculate_discount_amount(unit_of_measure, price_per_unit)
        amount = AmountCalculator(unit_of_measure, price_per_unit).calculate_amount()
        flat_discount_amount = (amount.value * self.discount_percent.value)/100
        return Currency(
            flat_discount_amount,
            amount.currency_code
        )

