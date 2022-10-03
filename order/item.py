from common.unit_of_measure import UnitOfMeasure
from store.store_product import StoreProduct


class Item:
    def __init__(self, product: StoreProduct, quantity: UnitOfMeasure):
        self.store_product = product
        self.quantity = quantity

