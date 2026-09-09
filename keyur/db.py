
from django.conf import settings

# Access the MongoDB database
db = settings.MONGO_DB

def get_all_products():
    return list(db.products.find())  # Fetch all products from MongoDB

def insert_product(name, price, stock):
    db.products.insert_one({"name": name, "price": price, "stock": stock})

def delete_product(product_id):
    db.products.delete_one({"_id": product_id})
