items = ["pen", "notebook", "charge", "scissors", "eraser", "backpack", "cap", "wallet"]
price = [1.99, .5, 4.99, 2.99, .45, 9.99, 7.99, 12.99]

pricelist = zip(items, price)
for k, v in pricelist:
    print(k, v)

cart = []
purchase = input("Enter the first item you would like to buy: ")
cart.append(purchase)
second = input("Enter another item: ")
cart.append(second)
third = input("Enter one last item: ")
cart.append(third)

prices = []
for k, v in pricelist:
    if k in cart:
        prices.append(v)
        # print(v)

total = 0
for p in prices:
    total += p

# print(cart)
# print(prices)
print(total)
