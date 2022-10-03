from order.item import Item
from typing import List


class Order:
    def __init__(self, items: List[Item]):
        self.items = items
