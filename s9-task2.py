def get_delivery_charge(amount,city='Ahmedabad'):
    if city=='Ahmedabad':
        return 30
    else:
        return 50

print(get_delivery_charge(1000))
print(get_delivery_charge(1000,'Surat'))