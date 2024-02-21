import requests
import json

class EventRetriever:
    def __init__(self, token_id):
        self.token_id = token_id
        self.events = []

        self.get_events()

    def get_events(self):
        headers = {"api-key": self.token_id}
        print("URL:")
        print("https://webhook.site/token/" + self.token_id + "/requests?sorting=newest")
        print()
        response = requests.get('https://webhook.site/token/'
                                + self.token_id 
                                +'/requests?sorting=newest', headers=headers)
        for event in response.json()["data"]:
            self.events.append(event)

    def __str__(self):
        s = ""
        for event in self.events:
            s += json.dumps(event, indent=4)
        return s