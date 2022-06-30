supermarket = {"milk": {"quantity": 20, "price": 1.19},
               "biscuits":  {"quantity": 32, "price": 1.45},
               "butter":  {"quantity": 20, "price": 2.29},
               "cheese":  {"quantity": 15, "price": 1.90},
               "bread":  {"quantity": 15, "price": 2.59},
               "cookies":  {"quantity": 20, "price": 4.99},
               "yogurt": {"quantity": 18, "price": 3.65},
               "apples":  {"quantity": 35, "price": 3.15},
               "oranges":  {"quantity": 40, "price": 0.99},
               "bananas": {"quantity": 23, "price": 1.29}}

total_value=0
for article,numbers in supermarket.items():
    quantity=numbers["quantity"]
    price=numbers["price"]
    product_price=quantity*price
    article=article+':'
    print(f"{article:15s}{product_price:08.2f}")
    total_value+=product_price
print("="*24)
print(f"total sum :{total_value:08.2f}")