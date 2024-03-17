from . import base
import requests

class PostHandler(base.Request):    

    def send(self):
        response = requests.post(self.url, data=self.data, headers=self.headers)
        return self.handleResponse(response)