import urllib.request
import json


class Response(object):
    def __init__(self, url, body, status_code):
        self.url = url
        self.body = body
        self.status_code = status_code

    def json(self):
        return json.loads(self.body)


def get(url, params=None):
    if params is not None:
        qs = urllib.parse.urlencode(params)
        url = f"{url}?{qs}"
    req = urllib.request.Request(url=url, method='GET')
    with urllib.request.urlopen(req) as f:
        return Response(url, f.read().decode('utf-8'), f.getcode())
