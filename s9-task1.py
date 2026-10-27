def calculate_final_price(price,discount_rate):
    discount=price*discount_rate
    return price - discount

print(calculate_final_price(1200,0.15))