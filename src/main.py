import json
import os
from event_handler import EventHandler
from agents.repair_agent import RepairAgent
from utils.git_handler import GitHandler
from utils.cache import DisabledCache
from config import Config, PromptConfig
from models import LLModel

events = json.loads(open("failed_check_runs.json").read())

# Arguments
git_user = os.environ["GIT_USERNAME"]
token = os.environ["GIT_ACCESS_TOKEN"]

# Information extracted from webhook
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

print("Log:\n", ag._failed_log)
print("Task:")
print(ag._tasks)

file_path = ag.find_file(
    gh.get_tmp_path(),
    ag.get_f_name(),
    ag.get_error_area()
    )
print(file_path)

ag.repair_file(file_path)
print("Response:\n", ag.get_response())

# Korrigierte Datei schreiben, commiten und pushen
gh.write_responses(
    [file_path],
    [ag.get_response()]
    )
commit_msg = ag.make_commit_msg()
gh.commit_and_push(
    [file_path],
    commit_msg
)

gh.create_pull_request(
    "Repairing broken CI/CD pipeline",
    commit_msg
)