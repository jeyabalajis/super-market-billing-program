from discount.discount_method import DiscountMethod


class Category:
    def __init__(self, name: str, discount_method: DiscountMethod):
        self.name = name
        self.discount_method = discount_method
