"""
This module provides the EventHandler class which is used to handle and 
process a GitHub webhook event (in particular a check run event).

The EventHandler class extracts necessary information from the event and 
provides a method to fetch the log of the failing job.
"""
import os
import requests

class EventHandler:
    """
    The EventHandler class is responsible for handling GitHub events.

    This class extracts necessary information from the event and provides a 
    method to fetch the log of the failing job.

    Attributes:
        repo_name (str): The name of the repository where the event occurred.
        owner_name (str): The owner of the repository.
        failing_branch (str): The branch where the failure occurred.
        failing_commit (str): The commit SHA where the failure occurred.
        failing_job_id (str): The ID of the failing job.
        log (str): The log of the failing job.
    """
    def __init__(self, event):
        """
        Initializes an EventHandler with the provided event.

        Args:
            event (dict): The event to handle.
        """
        self.repo_name = event["repository"]["name"]
        self.owner_name = event["repository"]["full_name"].split("/")[0]
        self.failing_branch = event["check_run"]["check_suite"]["head_branch"]
        self.failing_commit = event["check_run"]["check_suite"]["head_sha"]
        self.failing_job_id = event["check_run"]["details_url"].split("/")[-1]
        self.log = self.get_log()

    def get_log(self):
        """
        Fetches the log of the failing job.

        This method uses the GitHub API to fetch the log of the failing job.

        Returns:
            str: The log of the failing job.
        """
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
        """
        Returns a string representation of the EventHandler.

        Returns:
            str: A string representation of the EventHandler.
        """
        return (
            f"Repo Name: {self.repo_name}\n"
            f"Owner Name: {self.owner_name}\n"
            f"Failing Branch: {self.failing_branch}\n"
            f"Failing Commit: {self.failing_commit}\n"
            f"Failing Job ID: {self.failing_job_id}\n"
            f"Log:\n{self.log}\n"
        )