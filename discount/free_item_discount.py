from common.currency import Currency
from discount.discount_method import DiscountMethod
from common.unit_of_measure import UnitOfMeasure
from common.price_per_unit import PricePerUnit
from common.amount_calculator import AmountCalculator


class FreeItemDiscount(DiscountMethod):
    def __init__(self, *,
                 minimum_purchase_quantity: UnitOfMeasure, free_quantity: UnitOfMeasure):
        super().__init__()
        self.minimum_purchase_quantity = minimum_purchase_quantity
        self.free_quantity = free_quantity

    def calculate_discount_amount(self, unit_of_measure: UnitOfMeasure, price_per_unit: PricePerUnit) -> Currency:
        # iterate in portions of minimum_purchase_quantity
        remaining_quantity = unit_of_measure.value
        priced_quantity = 0

        while remaining_quantity >= self.minimum_purchase_quantity.value + self.free_quantity.value:
            priced_quantity += self.minimum_purchase_quantity.value
            remaining_quantity -= (self.minimum_purchase_quantity.value + self.free_quantity.value)

            print("priced: {}, remaining: {}".format(priced_quantity, remaining_quantity))

        priced_quantity += remaining_quantity

        print("original unit_of_measure: {}, priced unit_of_measure: {}".format(unit_of_measure.value, priced_quantity))
        priced_quantity_object = UnitOfMeasure((unit_of_measure.value - priced_quantity), unit_of_measure.uom_metric)
        return AmountCalculator(priced_quantity_object, price_per_unit).calculate_amount()
