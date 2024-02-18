def MaximumDiscount(n, prices):
    discount = 0
    while len(prices) >= 3:
        for i in range(3):
            price = max(prices)
            prices.remove(price)
            if i == 2:
                discount += price
    return discount
