import json

events = json.loads(open("failed_check_runs.json").read())

print("#Events:")
print(len(events))
print()

print("Keys first event:")
for key in events[0]:
    print(key)
print()

print("Check run status:")
print(events[0]["check_run"]["check_suite"]["status"])
print(events[0]["check_run"]["check_suite"]["conclusion"])
print()

print("Repository name:")
print(events[0]["repository"]["full_name"])
print()

print("Failing branch:")
print(events[0]["check_run"]["check_suite"]["head_branch"])
print()

print("Failing commit:")
print(events[0]["check_run"]["check_suite"]["head_sha"])