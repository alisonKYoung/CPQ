import mongo

class Server:
    def __init__(self):
        self.database = mongo.Database()
        self.database.db["Current Answers"].delete_many({})
        self.database.db["Results"].delete_many({})
        #temp
        self.database.db["Current Answers"].insert_one({"a1": True, "b0": "a", "c2": 4})