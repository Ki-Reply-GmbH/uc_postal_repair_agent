from config import PromptConfig
from models import LLModel

class RepairAgent:
    def __init__(self, prompts: PromptConfig, model: LLModel, failed_log: str):
        self._prompts = prompts
        self._model = model
        self._failed_log = failed_log #Currently a failing GitHub Actions workflow run

    def make_tasks(self):
        pass