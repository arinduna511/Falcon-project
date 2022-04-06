import falcon
import json
from helpers import save_to_db


class TimeStamp:
    def on_post(self, req, resp, timestamp, value):
        if timestamp and value:
            save_to_db(timestamp, value)
            resp.content_type = "application/json"
            resp.body = json.dumps({"timestamp": timestamp, "value": value})
            resp.status = falcon.HTTP_200

    def on_get(self, req, resp):
        for dt in TimeStamp.objects:
            d = {"data": [{"timestamp": dt.timestamp, "value": dt.value}]}
            resp.content_type = "application/json"
            resp.body = json.dumps(d)
            resp.status = falcon.HTTP_200


class Graph:

    def on_get(self, req, resp):
        for dt in TimeStamp.objects:
            d = {"data": [{"timestamp": dt.timestamp, "value": dt.value}]}
            resp.content_type = "application/json"
            resp.body = json.dumps(d)
            resp.status = falcon.HTTP_200
