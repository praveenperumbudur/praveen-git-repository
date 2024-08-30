import pandas as pd

class Product:
    def __init__(self, product_id, category, subcategory, price, quantity_sold):
        self.product_id = product_id
        self.category = category
        self.subcategory = subcategory
        self.price = price
        self.quantity_sold = quantity_sold

    def total_sales(self):
        return self.price * self.quantity_sold

# Example usage
product = Product('125', 'Electronics', 'Mobile', 500, 10)
print(product.total_sales())