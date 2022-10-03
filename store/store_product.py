from discount.discount_method import DiscountMethod
from product.product import Product
from common.price_per_unit import PricePerUnit
from store.store import Store


class StoreProduct:
    def __init__(self,
                 store: Store,
                 product: Product,
                 price_per_unit: PricePerUnit
                 ):
        self.store = store
        self.product = product
        self.price_per_unit = price_per_unit

