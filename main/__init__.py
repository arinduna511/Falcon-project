import falcon
from .views.datetime import TimeStamp, Graph


app = falcon.API()

ts = TimeStamp()

time_stamp = app.add_route("/api/timestamp/", ts)
time_stamp = app.add_route("/api/timestamp/{timestamp}/{value}/", ts)


gr = Graph()

app.add_route("/api/graph/", gr)
