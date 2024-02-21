from event_retriever import EventRetriever

events = EventRetriever("733cf8c8-554f-453c-8da2-8dffd77d349c")
events.write_events_to_file("events1.json")
print(events)