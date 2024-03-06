import json
from event_handler import EventHandler
from agents.repair_agent import RepairAgent
from utils.cache import DisabledCache
from config import Config, PromptConfig
from models import LLModel

events = json.loads(open("failed_check_runs.json").read())

infos = EventHandler(events[0])
print("Log:\n", infos.get_log())
print("Task:")
ag = RepairAgent(
    PromptConfig(),
    LLModel(
        Config(),
        DisabledCache(".")
        ),
    infos.get_log()
    )

print(ag.make_tasks())