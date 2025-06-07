import calc_points
from server import Server
server = Server()

calc = calc_points.CalcPoints(server)
pts = calc.calc_points()
server.database.db["Current Answers"].delete_many({})