import requests
import json

class EventRetriever:
    def __init__(self, url):
        self.url = url

    def get_events(self):
        response = requests.get(self.url)
        return json.loads(response.text)