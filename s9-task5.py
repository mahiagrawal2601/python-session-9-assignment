def calculate_cashback(amount,cashback_rate=0.05):
    return amount*cashback_rate

print(f"{calculate_cashback(500)} for a Zomato order")
print(f"{calculate_cashback(2000,0.07)} for a Flipkart order")