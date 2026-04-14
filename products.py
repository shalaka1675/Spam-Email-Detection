products = [
{"id":1,"name":"Laptop","category":"Electronics"},
{"id":2,"name":"Mouse","category":"Electronics"},
{"id":3,"name":"Keyboard","category":"Electronics"},
{"id":4,"name":"Headphones","category":"Electronics"},
{"id":5,"name":"Shoes","category":"Fashion"},
{"id":6,"name":"T-shirt","category":"Fashion"},
{"id":7,"name":"Jeans","category":"Fashion"},
{"id":8,"name":"Jacket","category":"Fashion"}
]

def recommend(id):
    # find selected product
    p = [x for x in products if x["id"] == id][0]

    # recommend same category products
    rec = [x for x in products if x["category"] == p["category"] and x["id"] != id]

    return rec