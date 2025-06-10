import yaml
from pymongo import MongoClient

class Database:
    def __init__(self):
        self.client = MongoClient("mongodb+srv://itzmind:ZVp41BnJG0WisQYw@evilsecrets.nbxj92y.mongodb.net/", 1678)
        self.db = self.client.Data

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

class Server:
    def __init__(self):
        self.database = Database()
        self.database.db["Results"].delete_many({})

server = Server()
class CalcPoints:
    def __init__(self, server):
        self.server = server

        with open("backend/questions.yaml", "r") as f:
            self.questions = yaml.load(f, yaml.Loader)
    
    def pull_data(self):
        answers = self.server.database.get_data("Current Answers")[0]
        return answers
    
    def calc_points(self):
        answers = self.pull_data()
        point_totals = {name: 0 for name in self.questions["names"]}
        print(answers)
        for question, vals in self.questions["answers"].items():
            answer = answers[question]
            if vals["type"] == "bool":
                if answer:
                    for person in vals["if_true"]:
                        point_totals[person] += vals["value"]
                else:
                    for person in vals["if_false"]:
                        point_totals[person] += vals["value"]
            else:
                if vals["type"] == "int":
                    answer = str(answer)
                for person in vals[answer]:
                    point_totals[person] += vals["value"]
        max_key = max(point_totals, key=point_totals.get)
        answers["winner"] = max_key
        self.server.database.upload_data("Results", {"winner": max_key})
        self.server.database.upload_data("Answers", answers)
        print(point_totals)
        return point_totals
    
calc = CalcPoints(server)
pts = calc.calc_points()
server.database.db["Current Answers"].delete_many({})