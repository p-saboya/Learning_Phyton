#Dictionaries list
items = [
    {
        "product" : "Shirt",
        "price" : 100
    },
    {
        "product" : "trousers",
        "price" : 200
    },
    {
        "product" : "scarf",
        "price" : 50
    }
    ]
prices = list(map(lambda item: item["price"], items))
print(prices) 

#Lambda functions --> ONLY one line

def add_taxes(item):
    item["taxes"] = item["price"] * 0.19
    return item

new_items = list(map(add_taxes, items))
print(new_items)
