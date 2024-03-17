from . import base
import requests

class GetHandler(base.Request):

    def send(self):
        response = requests.get(self.url, headers=self.headers)
        return self.handleResponse(response)