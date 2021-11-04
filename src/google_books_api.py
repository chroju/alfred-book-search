from requests import get


class GoogleBooksAPI(object):
    api_endpoint = 'https://www.googleapis.com/books/v1/volumes'

    def __init__(self):
        pass

    def search(self, query=""):
        payload = {
            'q': query,
            'maxResults': 15
        }
        return get(self.api_endpoint, params=payload)
