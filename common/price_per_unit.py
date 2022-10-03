from common.currency import Currency
from common.unit_of_measure import UnitOfMeasure


class PricePerUnit:
    def __init__(self, currency: Currency, uom: UnitOfMeasure):
        self.currency = currency
        self.uom = uom
