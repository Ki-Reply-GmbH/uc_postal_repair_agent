from config import PromptConfig
from models import LLModel

class RepairAgent:
    def __init__(self, prompts: PromptConfig, model: LLModel, failed_log: str):
        self._prompts = prompts
        self._model = model
        self._failed_log = failed_log #Currently a failing GitHub Actions workflow run
        self._tasks = self._make_tasks()

    def _make_tasks(self):
        tasks = self._model.get_completion(
            self._prompts.log_prompt.format(log=self._failed_log),
            "json_object"
            )
        return tasks
    
    