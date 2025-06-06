import yaml
from server import Server
class CalcPoints:
    def __init__(self):
        self.server = Server()

        with open("backend/questions.yaml", "r") as f:
            self.questions = yaml.load(f, yaml.Loader)
    
    def pull_data(self):
        answers = self.server.database.get_data("Current Answers")[0]
        return answers
    
    def calc_points(self):
        answers = self.pull_data()
        point_totals = {name: 0 for name in self.questions["names"]}
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
                if vals["type"] == "rating":
                    answer = str(answer)
                for person in vals[answer]:
                    point_totals[person] += vals["value"]
        print(point_totals)