from pymongo import MongoClient

class Database:
    def __init__(self):
        self.client = MongoClient("mongodb+srv://itzmind:ZVp41BnJG0WisQYw@evilsecrets.nbxj92y.mongodb.net/", 1678)
        self.db = self.client.Data

        #temp
        self.db["Current Answers"].insert_one({"a1": True, "b0": "a"})
    def get_data(self, collection, query = dict()):
        documents = list(self.db[collection].find(query))
        filtered = []
        for document in documents:
            document.pop("_id")
            filtered.append(document)
        return filtered
    def upload_data(self, collection, data):
        try:
            if isinstance(data, list) and data:
                self.db[collection].insert_many(data)
            elif data and isinstance(data, dict):
                self.db[collection].insert_one(data)
            else:
                print.warning(
                    f'Data for insertion to "{collection}" is not a list or dictionary, or is empty'
                )
        except Exception as err:
            print(f"Unable to insert some documents into collection {collection}: {err}")