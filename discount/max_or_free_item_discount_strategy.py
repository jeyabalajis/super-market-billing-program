from common.currency import Currency
from discount.free_item_discount import FreeItemDiscount
from order.item import Item
from discount.discount_strategy import DiscountStrategy
from common.currency_util import maximum


class MaxOrFreeItemDiscountStrategy(DiscountStrategy):
    """
    MaxOrFreeItemDiscountStrategy returns the free item discount amount, if the same is chosen for a product.
    Otherwise returns the maximum discount amount across product,sub-category and category.
    """
    def __init__(self):
        super().__init__()

    def calculate_discount_amount(self, item: Item) -> Currency:
        """
        If product employs free item discount, the same is chosen.
        Else maximum of product, sub category and category discount is chosen
        :return: Currency
        """
        super(MaxOrFreeItemDiscountStrategy, self).calculate_discount_amount(item)
        category_discount_method = item.store_product.product.category.discount_method
        category_discount_amount = category_discount_method.calculate_discount_amount(
            item.quantity,
            item.store_product.price_per_unit
        )

        sub_category_discount_method = item.store_product.product.sub_category.discount_method
        sub_category_discount_amount = sub_category_discount_method.calculate_discount_amount(
            item.quantity,
            item.store_product.price_per_unit
        )

        product_discount_method = item.store_product.product.discount_method
        product_discount_amount = product_discount_method.calculate_discount_amount(
            item.quantity,
            item.store_product.price_per_unit
        )

        if isinstance(product_discount_method, FreeItemDiscount):
            return product_discount_amount

        return maximum(
            [category_discount_amount, sub_category_discount_amount, product_discount_amount]
        )
