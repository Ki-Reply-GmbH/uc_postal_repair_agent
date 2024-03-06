import json
from event_handler import EventHandler

events = json.loads(open("failed_check_runs.json").read())

print(EventHandler(events[0]))