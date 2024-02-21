import requests
import json
import urllib.parse

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

    def write_events_to_file(self, filename):
        # Create a new list to hold the prettified events
        prettified_events = []

        # Iterate over the events
        for event in self.events:
            # Copy the event so we don't modify the original
            prettified_event = event.copy()

            # Prettify the 'content' field
            content = urllib.parse.unquote(prettified_event['content'])
            prettified_event['content'] = json.loads(content.replace('payload=', ''))

            # Add the prettified event to the new list
            prettified_events.append(prettified_event)

        # Write the prettified events to the file
        with open(filename, 'w') as f:
            json.dump(prettified_events, f, indent=4)

    def __str__(self):
        s = ""
        for event in self.events:
            s += json.dumps(event, indent=4)
        return s