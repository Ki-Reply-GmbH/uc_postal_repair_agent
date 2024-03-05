import os
import requests

class EventHandler:
    def __init__(self, event):
        self.repo_name = event["repository"]["name"]
        self.owner_name = event["repository"]["full_name"].split("/")[0]
        self.failing_branch = event["check_run"]["check_suite"]["head_branch"]
        self.failing_commit = event["check_run"]["check_suite"]["head_sha"]
        self.failing_job_id = event["check_run"]["details_url"].split("/")[-1]
        self.log = self.get_log()

    def get_log(self):
        token = os.environ["GIT_ACCESS_TOKEN"]
        headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json",
        }
        response = requests.get(
            f"https://api.github.com/repos/{self.owner_name}/{self.repo_name}/actions/jobs/{self.failing_job_id}/logs",
            headers=headers
        )
        return response.text

    def __str__(self):
        return (
            f"Repo Name: {self.repo_name}\n"
            f"Owner Name: {self.owner_name}\n"
            f"Failing Branch: {self.failing_branch}\n"
            f"Failing Commit: {self.failing_commit}\n"
            f"Failing Job ID: {self.failing_job_id}\n"
            f"Log:\n{self.log}\n"
        )