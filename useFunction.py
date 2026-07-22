def calculate_cart_total(cart):
    total = 0
    for item in cart:
        total += item["price"]*item["quantity"]
    return total


def calculate_cart_name(cart):
    for item in cart:
        print(item["name"])


cart = [
    {"name": "Keyboard", "price": 1500, "quantity": 2},
    {"name": "Mouse", "price": 700, "quantity": 1},
    {"name": "Monitor", "price": 12000, "quantity": 1}
]

a = calculate_cart_total(cart)
print("Total sum is ", a)

print(calculate_cart_total(cart))
print(calculate_cart_name(cart))
