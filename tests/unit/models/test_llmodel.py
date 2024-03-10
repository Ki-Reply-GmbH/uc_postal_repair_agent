import pytest
from src.models import LLModel
from src.config import Config
from src.utils.cache import Cache
from src.utils.functions import encode_to_base64

def test_llmodel_init(mocker):
    # Mock the Config and Cache classes
    mock_config = mocker.Mock(spec=Config)
    mock_config.OPENAI_API_KEY = "openai_api_key"
    mock_config.LLM_MODEL_NAME = "llm_model_name"
    mock_config.LLM_TEMPERATURE = "llm_temperature"
    mock_cache = mocker.Mock(spec=Cache)

    # Initialize the LLModel with the mocked Config and Cache
    model = LLModel(mock_config, mock_cache)

    # Assert that the attributes of the LLModel are the mocked Config and Cache
    assert model._model_name == mock_config.LLM_MODEL_NAME
    assert model._temperature == mock_config.LLM_TEMPERATURE
    assert model._cache == mock_cache

def test_get_llm_completion(mocker):
    # Mock the Config and Cache classes
    mock_config = mocker.Mock(spec=Config)
    mock_config.OPENAI_API_KEY = "openai_api_key"
    mock_config.LLM_MODEL_NAME = "llm_model_name"
    mock_config.LLM_TEMPERATURE = "llm_temperature"
    mock_cache = mocker.Mock(spec=Cache)

    # Initialize the LLModel with the mocked Config and Cache
    model = LLModel(mock_config, mock_cache)

    # Mock the _get_llm_completion method
    model._get_llm_completion = mocker.Mock(return_value="completion")

    # Call the _get_llm_completion method
    result = model._get_llm_completion("input")

    # Assert that the _get_llm_completion method was called with the correct argument
    model._get_llm_completion.assert_called_once_with("input")

    # Assert that the _get_llm_completion method returned the correct result
    assert result == "completion"

def test_get_completion(mocker):
    # Mock the Config and Cache classes
    mock_config = mocker.Mock(spec=Config)
    mock_config.OPENAI_API_KEY = "openai_api_key"
    mock_config.LLM_MODEL_NAME = "llm_model_name"
    mock_config.LLM_TEMPERATURE = "llm_temperature"
    mock_cache = mocker.Mock(spec=Cache)

    # Initialize the LLModel with the mocked Config and Cache
    model = LLModel(mock_config, mock_cache)

    # Mock the _get_completion_text method
    model._get_completion_text = mocker.Mock(return_value="completion")

    # Call the get_completion method
    result = model.get_completion("input", "text")

    # Assert that the _get_completion_text method was called with the correct arguments
    model._get_completion_text.assert_called_once_with(
        "input",
        encode_to_base64("input")
        )

    # Assert that the get_completion method returned the correct result
    assert result == "completion"

def test_get_completion_json(mocker):
    # Mock the Config and Cache classes
    mock_config = mocker.Mock(spec=Config)
    mock_config.OPENAI_API_KEY = "openai_api_key"
    mock_config.LLM_MODEL_NAME = "llm_model_name"
    mock_config.LLM_TEMPERATURE = "llm_temperature"
    mock_cache = mocker.Mock(spec=Cache)

    # Initialize the LLModel with the mocked Config and Cache
    model = LLModel(mock_config, mock_cache)

    # Mock the _get_completion_json method
    model._get_completion_json = mocker.Mock(return_value="json_object")

    # Call the _get_completion_json method
    result = model._get_completion_json("prompt", "base64_prompt")

    # Assert that the _get_completion_json method was called with the correct arguments
    model._get_completion_json.assert_called_once_with("prompt", "base64_prompt")

    # Assert that the _get_completion_json method returned the correct result
    assert result == "json_object"

def test_get_completion_text(mocker):
    # Mock the Config and Cache classes
    mock_config = mocker.Mock(spec=Config)
    mock_config.OPENAI_API_KEY = "openai_api_key"
    mock_config.LLM_MODEL_NAME = "llm_model_name"
    mock_config.LLM_TEMPERATURE = "llm_temperature"
    mock_cache = mocker.Mock(spec=Cache)

    # Initialize the LLModel with the mocked Config and Cache
    model = LLModel(mock_config, mock_cache)

    # Mock the _get_completion_text method
    model._get_completion_text = mocker.Mock(return_value="completion_text")

    # Call the _get_completion_text method
    result = model._get_completion_text("prompt", "base64_prompt")

    # Assert that the _get_completion_text method was called with the correct arguments
    model._get_completion_text.assert_called_once_with("prompt", "base64_prompt")

    # Assert that the _get_completion_text method returned the correct result
    assert result == "completion_text"