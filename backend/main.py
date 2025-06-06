import calc_points
from server import Server
server = Server()

def run():
    calc = calc_points.CalcPoints(server)
    pts = calc.calc_points()
    server.database.upload_data("Results", pts)
    return pts