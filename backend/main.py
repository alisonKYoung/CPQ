from pymongo import MongoClient
client = MongoClient("mongodb+srv://itzmind:ZVp41BnJG0WisQYw@evilsecrets.nbxj92y.mongodb.net/", 1678)
db = client.Data
collection = db.Answers
collection.insert_one({"hi": "ooo"})