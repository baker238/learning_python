def discounted(price, discount, max_discount=30, phone_name=''):
    price = abs(price)
    discount = abs(discount)
    max_discount = abs(max_discount)
    if max_discount >= 100:
        raise ValueError("Слишком большая максимальная скидка")
    elif discount >= max_discount:
        return price
    elif 'iphone' in phone_name.lower() or not phone_name:
        return price
    else:
        return price - (price * discount / 100)
new_price =discounted(100000, 10, phone_name='Iphone 12')
print(new_price)

new_price =discounted(70000, 25, phone_name='Samsung')
print(new_price)
new_price= discounted(5000, 5)
print(new_price)