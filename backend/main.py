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

        self.questions = {
            "answers": {
                "0": {
                    "type": "bool",
                    "value": 1,
                    "if_true": ["sarah"],
                    "if_false": ["alison"]
                },
                "1": {
                    "type": "bool",
                    "value": 1,
                    "if_true": ["amy"],
                    "if_false": ["alison"]
                },
                "2": {
                    "type": "bool",
                    "value": 1,
                    "if_true": ["alison"],
                    "if_false": ["scott", "amy"]
                },
                "3": {
                    "type": "bool",
                    "value": 1,
                    "if_true": ["blake"],
                    "if_false": ["alison", "scott", "sarah", "amy"]
                },
                "4": {
                    "type": "bool",
                    "value": 1,
                    "if_true": [],
                    "if_false": ["alison", "scott", "sarah", "amy", "blake"]
                },
                "6": {
                    "type": "bool",
                    "value": 1,
                    "if_true": ["alison", "amy", "sarah", "scott"],
                    "if_false": ["blake"]
                },
                "8": {
                    "type": "bool",
                    "value": 1,
                    "if_true": ["alison", "scott"],
                    "if_false": ["amy", "blake"]
                },
                "9": {
                    "type": "bool",
                    "value": 1,
                    "if_true": ["sarah"],
                    "if_false": ["scott"]
                },
                "10": {
                    "type": "bool",
                    "value": 1,
                    "if_true": ["amy"],
                    "if_false": ["sarah", "alison"]
                },
                "11": {
                    "type": "bool",
                    "value": 1,
                    "if_true": ["amy"],
                    "if_false": ["blake"]
                },
                "12": {
                    "type": "str",
                    "value": 1,
                    "A": ["alison"],
                    "B": [],
                    "C": ["scott", "amy"],
                    "D": []
                },
                "13": {
                    "type": "str",
                    "value": 1,
                    "A": [],
                    "B": [],
                    "C": ["amy"],
                    "D": ["alison", "scott"]
                },
                "14": {
                    "type": "bool",
                    "value": 1,
                    "if_true": ["blake", "sarah", "scott"],
                    "if_false": ["alison", "amy"]
                },
                "15": {
                    "type": "bool",
                    "value": 1,
                    "if_true": ["alison"],
                    "if_false": ["amy"]
                },
                "16": {
                    "type": "bool",
                    "value": 1,
                    "if_true": ["alison", "scott", "sarah"],
                    "if_false": ["blake", "amy"]
                },
                "20": {
                    "type": "bool",
                    "value": 1,
                    "if_true": [],
                    "if_false": ["alison", "scott"]
                },
                "21": {
                    "type": "int",
                    "value": 1,
                    "1": ["alison", "amy"],
                    "2": [],
                    "3": ["blake"],
                    "4": [],
                    "5": ["scott", "sarah"]
                },
                "22": {
                    "type": "int",
                    "value": 1,
                    "1": [],
                    "2": ["scott"],
                    "3": [],
                    "4": [],
                    "5": ["alison", "amy"]
                },
                "23": {
                    "type": "int",
                    "value": 1,
                    "1": [],
                    "2": [],
                    "3": [],
                    "4": [],
                    "5": ["alison", "scott", "amy"]
                },
                "24": {
                    "type": "bool",
                    "value": 1,
                    "if_true": ["alison"],
                    "if_false": ["scott", "blake"]
                },
                "25": {
                    "type": "bool",
                    "value": 1,
                    "if_true": ["sarah"],
                    "if_false": ["alison", "scott"]
                },
                "26": {
                    "type": "bool",
                    "value": 1,
                    "if_true": ["scott", "amy"],
                    "if_false": ["alison"]
                },
                "27": {
                    "type": "bool",
                    "value": 1,
                    "if_true": ["amy"],
                    "if_false": ["blake"]
                },
                "29": {
                    "type": "int",
                    "value": 1,
                    "1": [],
                    "2": ["amy"],
                    "3": [],
                    "4": ["scott"],
                    "5": ["alison"]
                },
                "30": {
                    "type": "int",
                    "value": 1,
                    "1": ["alison", "scott"],
                    "2": ["sarah"],
                    "3": ["amy"],
                    "4": [],
                    "5": ["blake"]
                },
                "31": {
                    "type": "bool",
                    "value": 1,
                    "if_true": ["amy"],
                    "if_false": ["alison"]
                },
                "32": {
                    "type": "bool",
                    "value": 1,
                    "if_true": ["amy", "alison"],
                    "if_false": ["scott", "blake"]
                },
                "33": {
                    "type": "bool",
                    "value": 1,
                    "if_true": ["alison"],
                    "if_false": ["scott"]
                },
                "34": {
                    "type": "str",
                    "value": 1,
                    "A": ["alison", "scott"],
                    "B": [],
                    "C": [],
                    "D": []
                }
            },
            "names": ["alison", "amy", "blake", "sarah", "scott"]
        }
    
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