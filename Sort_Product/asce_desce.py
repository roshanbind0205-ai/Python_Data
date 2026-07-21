from functools import cmp_to_key
products=[
    {"name":"keyboard","price": 800 , "rating": 4.5},
    {"name": "mouse", "price": 500, "rating": 4.2},
    {"name":"monitor","price": 400,"rating":4.0},
    {"name": "USB cable", "price": 1000, "rating": 4.1},
]
def compare_products(a,b):
    if a["price"] != b["price"]:
        return a["price"] - b["price"]
    if a["rating"] > b["rating"]:
        return -1
    elif a["rating"]<b["ratting"]:
        return 1
    else:
        return 0
        
products.sort(key=cmp_to_key(compare_products))
for product in products:
    print(product["name"],product["price"],product["rating"])