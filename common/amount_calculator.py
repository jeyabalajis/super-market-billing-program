from common.unit_of_measure import UnitOfMeasure
from common.price_per_unit import PricePerUnit
from common.currency import Currency


class AmountCalculator:
    def __init__(self, unit_of_measure: UnitOfMeasure, price_per_unit: PricePerUnit):
        self.unit_of_measure = unit_of_measure
        self.price_per_unit = price_per_unit

    def calculate_amount(self) -> Currency:
        if str(self.unit_of_measure.uom_metric) == str(self.price_per_unit.uom.uom_metric):
            return Currency(
                self.unit_of_measure.value * self.price_per_unit.currency.value,
                self.price_per_unit.currency.currency_code
            )

