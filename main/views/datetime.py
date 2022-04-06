import falcon
import json


class TimeStamp:
    def on_post(self, req, resp, timestamp, value):
        if timestamp and value:
            ts = TimeStamp(timestamp, value)
            ts.save()
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
