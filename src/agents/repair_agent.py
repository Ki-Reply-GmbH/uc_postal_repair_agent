import os
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
    
    def _find_file(path, file_name, file_content):
        for root, _, files in os.walk(path):
            if file_name in files:
                with open(os.path.join(root, file_name), "r") as file:
                    if file_content in file.read():
                        return os.path.join(root, file_name)
        return None