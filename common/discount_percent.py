class DiscountPercent:
    def __init__(self, value: float):
        assert 0.0 <= value <= 100.0
        self.value = value
