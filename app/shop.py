import datetime


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def shopping_cost(self, product_cart: dict) -> float:
        for product in product_cart:
            if product not in self.products:
                return None
        total = 0
        for product, qty in product_cart.items():
            price = self.products[product]
            total += price * qty
        return total

    def print_receipt(self, product_cart: dict, customer_name: str) -> None:
        print(f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")
        for product, quantity in product_cart.items():
            cost = self.products[product] * quantity
            if cost.is_integer():
                cost = int(cost)
            print(f"{quantity} {product}s for "
                  f"{cost:.2f} dollars")
        total = self.shopping_cost(product_cart)
        total = int(total)
        print(f"Total cost is {total:.2f} dollars")
        print("See you again!")
