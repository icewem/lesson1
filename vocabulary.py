phones=["iPhone Xs", "Samsung 19s", "Xiaomi Mi8"]

product = {
    "name": "iPhone X",
    "stock": 5,
    "price": 66000.0,
    "recomend": phones
    }


product['memory'] = 10
print(product)
#print(product.get("memory"))
#del product["stock"]
#product["recomend"]= phones

print(product["recomend"][1:3])
print(product)
product["recomend"].append("Sony X")
print(product)