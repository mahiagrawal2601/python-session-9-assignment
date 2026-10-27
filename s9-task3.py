def format_coupon_message(username,discount=10):
    return f"Hi {username}, you get {discount}% off!"

print(format_coupon_message('Rahul'))
print(format_coupon_message('Mahi',15))