from unittest import TestCase
from common.unit_of_measure import UnitOfMeasure


class TestQuantity(TestCase):
    def test_quantity(self):
        quantity_10_kg = UnitOfMeasure(10.0, UnitOfMeasure.KILO)
        assert quantity_10_kg.uom_metric == "KG"

