class UnitOfMeasure:
    KILO = "KG"

    def __init__(self, value: float, uom_metric: str):
        """abstract base class"""
        self.value = value
        assert uom_metric in [self.KILO]
        self.uom_metric = uom_metric

