def MaximumDiscount(n, prices):
    discount = 0
    while len(prices) > 3:
        for i in range(3):
            price = max(prices)
            prices.remove(price)
            if i == 2:
                discount += price
    return discount

print(MaximumDiscount(7, [400, 350, 300, 250, 200, 150, 100]))


