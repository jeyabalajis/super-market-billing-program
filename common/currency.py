class Currency:

    INR = "Indian Rupees"

    def __init__(self, value: float, currency_code: str):
        self.value = value
        assert currency_code in [self.INR]
        self.currency_code = currency_code

