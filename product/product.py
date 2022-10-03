from discount.discount_method import DiscountMethod
from product.category import Category
from product.sub_category import SubCategory


class Product:
    def __init__(self,
                 name: str,
                 category: Category,
                 sub_category: SubCategory,
                 discount_method: DiscountMethod,
                 ):
        self.name = name
        self.category = category
        self.sub_category = sub_category
        self.discount_method = discount_method
