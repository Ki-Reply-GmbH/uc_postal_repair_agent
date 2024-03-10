
import os
import tempfile
import git
import datetime
import uuid
import shutil
from freezegun import freeze_time
from src.utils.git_handler import GitHandler
from unittest.mock import patch

def test_get_tmp_path():
    # Initialize the GitHandler
    git_handler = GitHandler()

    # Set the _tmp_path attribute
    git_handler._tmp_path = "/tmp/path"

    # Call the get_tmp_path method
    result = git_handler.get_tmp_path()

    # Assert that the get_tmp_path method returned the correct result
    assert result == "/tmp/path"

def test_initialize():
    project_root_dir = os.path.dirname(
        os.path.dirname(
            os.path.dirname(
                os.path.dirname(
                    os.path.abspath(__file__)
                )
            )
        )
    )
    # Initialize the GitHandler with all attributes
    git_handler = GitHandler()

    # Call the initialize method
    git_handler.initialize(
        branch="branch",
        git_user="user",
        owner="owner",
        token="token",
        repo_name="repo"
    )

    # Assert that the GitHandler attributes are correctly set
    assert git_handler._tmp_path == os.path.join(project_root_dir, ".tmp")
    assert git_handler._branch == "branch"
    assert git_handler._git_user == "user"
    assert git_handler._owner == "owner"
    assert git_handler._token == "token"
    assert git_handler._repo_name == "repo"

from freezegun import freeze_time

@freeze_time("2022-01-01")
def test_clone(mocker):
    # Mock the Repo.clone_from method
    mocker.patch("git.Repo.clone_from", return_value=mocker.MagicMock())

    # Mock the uuid4 method
    mocker.patch("uuid.uuid4", return_value="mocked_uuid4")

    # Initialize the GitHandler with all attributes
    git_handler = GitHandler()

    # Call the initialize method
    git_handler.initialize(
        branch="branch",
        git_user="user",
        owner="owner",
        token="token",
        repo_name="repo"
    )

    # Call the clone method
    git_handler.clone()

    # Assert that the Repo.clone_from method was called
    git.Repo.clone_from.assert_called_once_with(
        "https://user:token@github.com/owner/repo.git",
        git_handler._tmp_path
    )

    # Assert that _unique_feature_branch_name is set correctly
    #assert git_handler._unique_feature_branch_name == 

def test_clean_up(mocker):
    # Mock the os.path.exists method to return True
    mocker.patch("os.path.exists", return_value=True)

    # Mock the os.walk method to return a generator that yields a tuple with a root, dirs, and files
    mocker.patch("os.walk", return_value=[("/tmp/path", ["dir"], ["file"])])

    # Mock the os.chmod and shutil.rmtree methods
    mocker.patch("os.chmod")
    mocker.patch("shutil.rmtree")

    # Initialize the GitHandler
    git_handler = GitHandler()

    # Set the _tmp_path attribute
    git_handler._tmp_path = "/tmp/path"

    # Call the clean_up method
    git_handler.clean_up()

    # Assert that the os.path.exists method was called with the correct argument
    os.path.exists.assert_called_once_with("/tmp/path")

    # Assert that the os.walk method was called with the correct argument
    os.walk.assert_called_once_with("/tmp/path")

    # Assert that the os.chmod method was called twice (once for the directory and once for the file)
    assert os.chmod.call_count == 2

    # Assert that the shutil.rmtree method was called with the correct argument
    shutil.rmtree.assert_called_once_with("/tmp/path")

def test_write_responses(mocker):
    # Mock the open function
    open_mock = mocker.mock_open()
    mocker.patch("builtins.open", open_mock)

    # Initialize the GitHandler
    git_handler = GitHandler()

    # Set the _tmp_path attribute
    git_handler._tmp_path = "/tmp/path"

    # Define the file_paths and responses
    file_paths = ["file1.txt", "file2.txt"]
    responses = ["response1", "response2"]

    # Call the write_responses method
    git_handler.write_responses(file_paths, responses)

    # Assert that the open function was called with the correct arguments
    open_mock.assert_any_call(os.path.join("/tmp/path", "file1.txt"), "w")
    open_mock.assert_any_call(os.path.join("/tmp/path", "file2.txt"), "w")

    # Assert that the write method was called with the correct arguments
    open_mock().write.assert_any_call("response1")
    open_mock().write.assert_any_call("response2")

@patch("requests.post")
def test_create_pull_request_success(mock_post):
    # Mock the requests.post method to return a successful response
    mock_post.return_value.status_code = 201
    mock_post.return_value.json.return_value = {"id": 1}

    # Initialize the GitHandler with all attributes
    git_handler = GitHandler()

    # Call the create_pull_request method
    response = git_handler.create_pull_request("title", "body")

    # Assert that the response is correct
    assert response == {"id": 1}

@patch("requests.post")
def test_create_pull_request_failure(mock_post):
    # Mock the requests.post method to return a failure response
    mock_post.return_value.status_code = 400
    mock_post.return_value.json.return_value = {"message": "error"}

    # Initialize the GitHandler with all attributes
    git_handler = GitHandler()

    # Call the create_pull_request method
    response = git_handler.create_pull_request("title", "body")

    # Assert that the response is correct
    assert response == {"message": "error"}