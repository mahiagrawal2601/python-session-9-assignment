def apply_discount(price,rate=0.10):
    discount = price*rate
    return price-discount

print(apply_discount(10000))