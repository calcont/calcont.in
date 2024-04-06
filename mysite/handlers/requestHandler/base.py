from django.http import HttpResponse
from abc import ABC, abstractmethod


class Request(ABC):
    def __init__(self, url, data=None, headers=None):
        self.url = url
        self.data = data
        self.headers = headers

    @abstractmethod
    def send(self):
        pass

    def handleResponse(self, response):
        if response.status_code != 200:
            return HttpResponse(f"An error occurred: {response.status_code}")
        return response
