shop_name = "Nihal's Shop"
is_open = True

products = {
    "Rice": {"price": 65.0, "stock": 50},
    "Dal": {"price": 40, "stock": 20},
    "Oil": {"price": 70, "stock": 90}
}

print(f"--- {shop_name} you are welcome")
customer_name = input("Enter your name:")

print(f"Hello {customer_name} this is our product list -")
for item, info in products.items():
    print(f"{item}: price {info['price']} taka(stock: {info['stock']}")

total_bill = 0.0
while True:
    choice = input("Which product you want to purchase(if you dont want thern write "exit")")

    if choice.lowe() == 'exit':
        break
    if choice in products:
        quantity = int(input(f"how much kg/L {choice}"))