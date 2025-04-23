import datetime
from dataclasses import dataclass

@dataclass
class Sale:
    product_number: int
    retailer_code: int
    order_method_code: int
    date: datetime.date
    quantity: int
    unit_price: float
    unit_sale_price: float

    def __post_init__(self):
        self.ricavo: float = self.quantity * self.unit_sale_price

    def __hash__(self):
        return hash(self.product_number), hash(self.retailer_code), hash(self.order_method_code)

    def __eq__(self, other):
        return (self.product_number == other.product_number,
                self.retailer_code == other.retailer_code,
                self.order_method_code == other.order_method_code)

    def __str__(self):
        return f"Data: {self.date}, ricavo: {self.ricavo}, prodotto {self.product_number}, retailer: {self.retailer_code}"