import json
import os
from event_handler import EventHandler
from agents.repair_agent import RepairAgent
from utils.git_handler import GitHandler
from utils.cache import DisabledCache
from config import Config, PromptConfig
from models import LLModel

import pprint

def main():
    # Arguments
    git_user = os.environ["GIT_USERNAME"]
    token = os.environ["GIT_ACCESS_TOKEN"]

    # Information extracted from webhook
    #TODO Mit Azure EventHub extrahieren
    owner = "TimoKubera"
    repo = "broken_webhooks"
    branch = "main"

    # Initialize GitHandler
    gh = GitHandler()
    gh.initialize(
        branch,
        git_user,
        owner,
        token,
        repo
    )
    gh.clean_up()
    gh.clone()

    # Load events
    events = json.loads(open("failed_check_runs.json").read())

    # Initialize RepairAgent
    infos = EventHandler(events[0])
    ag = RepairAgent(
        PromptConfig(),
        LLModel(
            Config(),
            DisabledCache(".")
        ),
        infos.get_log()
    )
    """
    # Find file and repair
    file_path = ag.find_file(
        gh.get_tmp_path(),
        ag.get_f_name(),
        ag.get_error_area()
    )
    ag.repair_file(file_path)

    # Write responses, commit and push
    gh.write_responses(
        [file_path],
        [ag.get_response()]
    )
    commit_msg = ag.make_commit_msg()
    gh.commit_and_push(
        [file_path],
        commit_msg
    )

    # Create pull request
    gh.create_pull_request(
        "Repairing broken CI/CD pipeline",
        commit_msg
    )
    """
    workflows = [
        "C:\\Users\\t.kubera\\dev\\dhl\\uc_postal_repair_agent\\tests\\workflow1.yaml",
        "C:\\Users\\t.kubera\\dev\\dhl\\uc_postal_repair_agent\\tests\\workflow2.yaml",
        "C:\\Users\\t.kubera\\dev\\dhl\\uc_postal_repair_agent\\tests\\workflow3.yaml",
        "C:\\Users\\t.kubera\\dev\\dhl\\uc_postal_repair_agent\\tests\\workflow4.yaml"
    ]
    jobs = ag._extract_jobs_from_github_actions(workflows)
    pprint.pprint(jobs)

if __name__ == "__main__":
    main()