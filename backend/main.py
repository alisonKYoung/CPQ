import calc_points
from server import Server
server = Server()

calc = calc_points.CalcPoints(server)
pts = calc.calc_points()
max_key = max(pts, key=pts.get)
server.database.upload_data("Results", {"winner": max_key})
server.database.db["Current Answers"].delete_many({})