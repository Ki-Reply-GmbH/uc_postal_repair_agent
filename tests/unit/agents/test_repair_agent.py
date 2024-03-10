import pytest
import os
import tempfile
from src.agents.repair_agent import RepairAgent
from src.config import Config, PromptConfig
from src.models import LLModel
from src.utils.cache import DisabledCache

def test_repair_agent_initialization(mocker):
    config = Config()
    cache = DisabledCache(".")
    model = LLModel(config, cache)
    prompt_config = PromptConfig()
    log = "log"

    mocker.patch.object(
        RepairAgent,
        "_make_tasks",
        return_value="mocked tasks"
        )

    ag = RepairAgent(prompt_config, model, log)

    assert isinstance(ag, RepairAgent)
    assert ag._prompts == prompt_config
    assert ag._model == model
    assert ag._failed_log == log
    assert ag._tasks == "mocked tasks"

    assert isinstance(ag, RepairAgent)
    assert ag._prompts == prompt_config
    assert ag._model == model
    assert ag._failed_log == log
    assert ag._tasks == "mocked tasks"

def test_get_f_name():
    ag = RepairAgent(
        PromptConfig(),
        LLModel(
            Config(),
            DisabledCache(".")
        ),
        "log"
    )

    # Set the tasks for the test
    ag._tasks = {
        "file": "file for testing"
    }

    assert ag.get_f_name() == "file for testing"

def test_get_explanation():
    ag = RepairAgent(
        PromptConfig(),
        LLModel(
            Config(),
            DisabledCache(".")
        ),
        "log"
    )

    # Set the tasks for the test
    ag._tasks = {
        "explanation": "mocked explanation"
    }

    assert ag.get_explanation() == "mocked explanation"

def test_get_error_area():
    ag = RepairAgent(
        PromptConfig(),
        LLModel(
            Config(),
            DisabledCache(".")
        ),
        "log"
    )

    # Set the tasks for the test
    ag._tasks = {
        "error_area": "mocked error area"
    }

    assert ag.get_error_area() == "mocked error area"

def test_get_response():
    ag = RepairAgent(
        PromptConfig(),
        LLModel(
            Config(),
            DisabledCache(".")
        ),
        "log"
    )

    # Set the response for the test
    ag._response = "mocked response"

    assert ag.get_response() == "mocked response"

def test_make_tasks(mocker):
    ag = RepairAgent(
        PromptConfig(),
        LLModel(
            Config(),
            DisabledCache(".")
        ),
        "log"
    )

    # Mock the get_completion method of the model
    mocker.patch.object(
        LLModel,
        "get_completion",
        return_value="mocked tasks"
    )

    tasks = ag._make_tasks()

    assert tasks == "mocked tasks"

def test_find_file():
    ag = RepairAgent(
        PromptConfig(),
        LLModel(
            Config(),
            DisabledCache(".")
        ),
        "log"
    )

    # Create a temporary directory
    with tempfile.TemporaryDirectory() as tmp_dir:
        # Create a file with the specified name and content
        file_name = "test_file.txt"
        file_content = "test content"
        file_path = os.path.join(tmp_dir, file_name)
        with open(file_path, "w") as file:
            file.write(file_content)

        # Test the find_file method
        found_file_path = ag.find_file(tmp_dir, file_name, file_content)
        assert found_file_path == file_path

def test_repair_file(mocker):
    ag = RepairAgent(
        PromptConfig(),
        LLModel(
            Config(),
            DisabledCache(".")
        ),
        "log"
    )

    # Mock the get_completion method of the model
    mocker.patch.object(
        LLModel,
        "get_completion",
        return_value="mocked response"
    )

    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(b"test content")

    # Test the repair_file method
    ag.repair_file(tmp_file.name)

    assert ag._response == "mocked response"

def test_make_commit_msg(mocker):
    ag = RepairAgent(
        PromptConfig(),
        LLModel(
            Config(),
            DisabledCache(".")
        ),
        "log"
    )

    # Mock the get_completion method of the model
    mocker.patch.object(
        LLModel,
        "get_completion",
        return_value="mocked commit message"
    )

    # Test the make_commit_msg method
    commit_msg = ag.make_commit_msg()

    assert commit_msg == "mocked commit message"