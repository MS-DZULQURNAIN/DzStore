from pymongo import MongoClient

# Menghubungkan ke MongoDB
client = MongoClient("mongodb+srv://avel:tmp0@aveltmp.nqyqy6h.mongodb.net/aveltmp?retryWrites=true&w=majority:27017/")

# Memilih database
db = client["DzStore"]

def add_topup(user_id, amount):
    collection = db["topup"]
    data = {"user_id": user_id, "amount": amount}
    collection.insert_one(data)

def get_topup(user_id):
    collection = db["topup"]
    data = collection.find_one({"user_id": user_id})
    return data["amount"] if data else 0

def add_coin(user_id, coins):
    collection = db["coin"]
    data = {"user_id": user_id, "coins": coins}
    collection.insert_one(data)

def get_coin(user_id):
    collection = db["coin"]
    data = collection.find_one({"user_id": user_id})
    return data["coins"] if data else 0
