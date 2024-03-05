import requests
import json

# Send a GET request to the local server
response = requests.get("http://127.0.0.1:3000/")

# Parse the JSON response
data = response.json()

# Filter the check_run messages
check_run_messages = [item for item in data if "check_run" in item]

# Filter failed check_run messages and ignore organzation check_run messages
failed_check_run_messages = [item for item in check_run_messages if 
                             item["check_run"]["conclusion"] == "failure"]

# Write the failed check_run messages to a JSON file
with open("failed_check_runs.json", "w") as f:
    json.dump(failed_check_run_messages, f, indent=4)