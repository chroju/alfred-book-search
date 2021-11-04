from requests import get


class OpenBDAPI(object):
    api_endpoint = 'https://api.openbd.jp/v1/get'

    def __init__(self):
        pass

    def get(self, isbn=""):
        payload = {
            'isbn': isbn
        }
        return get(self.api_endpoint, params=payload)
