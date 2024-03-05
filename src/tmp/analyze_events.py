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
repo = events[0]["repository"]["name"]
print(repo)
print(events[0]["repository"]["full_name"])
print()

print("Failing branch:")
print(events[0]["check_run"]["check_suite"]["head_branch"])
print()

print("Failing commit:")
print(events[0]["check_run"]["check_suite"]["head_sha"])
print()

print("Failing job id:")
url = events[0]["check_run"]["details_url"]
job_id = url.split("/")[-1]
print(job_id)
print()


# Analyze the logs of the failing job
import requests
import os

# Replace with your personal access token
token = os.environ["GIT_ACCESS_TOKEN"]
owner = os.environ["GIT_USERNAME"]

headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github.v3+json",
}

response = requests.get(
    f"https://api.github.com/repos/{owner}/{repo}/actions/jobs/{job_id}/logs",
    headers=headers
    )

# The logs are returned as plain text
print("Failing job logs:")
logs = response.text
print(response.status_code)
print(response.headers)
print(logs)