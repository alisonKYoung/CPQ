import mongo

class Server:
    def __init__(self):
        self.db = mongo.Database()