from event_retriever import EventRetriever

events = EventRetriever("https://webhook.site/733cf8c8-554f-453c-8da2-8dffd77d349c").get_events()

print(events)