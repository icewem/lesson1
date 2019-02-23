#price = 100
#discount = 10

#price_witch_discount = price - price * discount / 100

#print(price_witch_discount)


def discounted(price,discount,max_discount=50):
    price  = abs(float(price))
    discount = abs(float(discount))
    max_discount = abs(float(max_discount))
    if max_discount > 99:
          raise ValueError("Максимальная скидка не может быть больше 99%")
    if discount >= max_discount:
        price_witch_discount = price
    else:
        price_witch_discount = price - price * discount / 100
    return(price_witch_discount)

#product = {
#    "name": "iPhone X",
#    "stock": 5,
#    "price": 66000.0,
#    "discount": 70
#    }
#discounted(100, 50, max_discount=100)
print(discounted(100,40))