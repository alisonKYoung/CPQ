import mongo

class Server:
    def __init__(self):
        self.database = mongo.Database()
        self.database.db["Results"].delete_many({})