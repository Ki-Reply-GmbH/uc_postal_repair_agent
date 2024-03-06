#
# This code is protected by intellectual property rights.
# Dr. Ing. h.c. F. Porsche AG owns exclusive rights of use.
# © 2019-2023, Dr. Ing. h.c. F. Porsche AG.
#

import logging
import os
import sys
import tempfile
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()

LOGGER = logging.getLogger(__name__)
logging.basicConfig(level=os.environ.get("LOG_LEVEL", "INFO"))


@dataclass
class PromptConfig:
    def __init__(self):
        self.log_prompt = log_prompt
        self.repair_prompt = repair_prompt
        self.commit_prompt = commit_prompt

log_prompt = """\
You will receive the log of a failed CI/CD pipeline. The log contains \
unnecessary information.
1. Search for the relevant information that describes the cause of the error.
2. Summarize the cause of the error so that another LLM can correct the error \
based on this summary.
3. Identify the files in which the error is caused and which need to be \
corrected.
4. Return a Json file with the keys "relevant_infos", "explanation" and "files".\
The cause of the error (str), as described in 2., should be in "Explanation". \
A list of files that trigger the error should be stored in "Files".

Log:
 ï»¿2024-03-05T12:15:14.3880589Z Current runner version: '2.314.1'
2024-03-05T12:15:14.3912333Z ##[group]Operating System
2024-03-05T12:15:14.3913165Z Ubuntu
2024-03-05T12:15:14.3913813Z 22.04.4
2024-03-05T12:15:14.3914294Z LTS
2024-03-05T12:15:14.3914765Z ##[endgroup]
2024-03-05T12:15:14.3915323Z ##[group]Runner Image
2024-03-05T12:15:14.3915942Z Image: ubuntu-22.04
2024-03-05T12:15:14.3916515Z Version: 20240225.1.0
2024-03-05T12:15:14.3917999Z Included Software: https://github.com/actions/runner-images/blob/ubuntu22/20240225.1/images/ubuntu/Ubuntu2204-Readme.md
2024-03-05T12:15:14.3919986Z Image Release: https://github.com/actions/runner-images/releases/tag/ubuntu22%2F20240225.1
2024-03-05T12:15:14.3921201Z ##[endgroup]
2024-03-05T12:15:14.3921850Z ##[group]Runner Image Provisioner
2024-03-05T12:15:14.3922557Z 2.0.359.1
2024-03-05T12:15:14.3923018Z ##[endgroup]
2024-03-05T12:15:14.3924423Z ##[group]GITHUB_TOKEN Permissions
2024-03-05T12:15:14.3926872Z Contents: read
2024-03-05T12:15:14.3927623Z Metadata: read
2024-03-05T12:15:14.3928437Z Packages: read
2024-03-05T12:15:14.3929121Z ##[endgroup]
2024-03-05T12:15:14.3933082Z Secret source: Actions
2024-03-05T12:15:14.3933906Z Prepare workflow directory
2024-03-05T12:15:14.4695547Z Prepare all required actions
2024-03-05T12:15:14.4888507Z Getting action download info
2024-03-05T12:15:14.6541176Z Download action repository 'actions/checkout@v2' (SHA:ee0669bd1cc54295c223e0bb666b733df41de1c5)
2024-03-05T12:15:14.9348908Z Complete job name: build
2024-03-05T12:15:15.0411740Z ##[group]Run actions/checkout@v2
2024-03-05T12:15:15.0412392Z with:
2024-03-05T12:15:15.0413109Z   token: ***
2024-03-05T12:15:15.0413599Z   repository: SomeOwner/SomeRepo
2024-03-05T12:15:15.0414241Z   ssh-strict: true
2024-03-05T12:15:15.0414703Z   persist-credentials: true
2024-03-05T12:15:15.0415231Z   clean: true
2024-03-05T12:15:15.0415638Z   fetch-depth: 1
2024-03-05T12:15:15.0416060Z   lfs: false
2024-03-05T12:15:15.0416451Z   submodules: false
2024-03-05T12:15:15.0416927Z   set-safe-directory: true
2024-03-05T12:15:15.0417454Z ##[endgroup]
2024-03-05T12:15:15.3693973Z Syncing repository: SomeOwner/SomeRepo
2024-03-05T12:15:15.3696341Z ##[group]Getting Git version info
2024-03-05T12:15:15.3697452Z Working directory is '/home/runner/work/SomeRepo/SomeRepo'
2024-03-05T12:15:15.3698715Z [command]/usr/bin/git version
2024-03-05T12:15:15.3858670Z git version 2.43.2
2024-03-05T12:15:15.3885930Z ##[endgroup]
2024-03-05T12:15:15.3904394Z Temporarily overriding HOME='/home/runner/work/_temp/f596c1c4-b9e1-46e0-b90d-ea1163081438' before making global git config changes
2024-03-05T12:15:15.3906227Z Adding repository directory to the temporary git global config as a safe directory
2024-03-05T12:15:15.3908788Z [command]/usr/bin/git config --global --add safe.directory /home/runner/work/SomeRepo/SomeRepo
2024-03-05T12:15:15.3956440Z Deleting the contents of '/home/runner/work/SomeRepo/SomeRepo'
2024-03-05T12:15:15.3961679Z ##[group]Initializing the repository
2024-03-05T12:15:15.3966061Z [command]/usr/bin/git init /home/runner/work/SomeRepo/SomeRepo
2024-03-05T12:15:15.4062417Z hint: Using 'master' as the name for the initial branch. This default branch name
2024-03-05T12:15:15.4063927Z hint: is subject to change. To configure the initial branch name to use in all
2024-03-05T12:15:15.4065469Z hint: of your new repositories, which will suppress this warning, call:
2024-03-05T12:15:15.4066424Z hint:
2024-03-05T12:15:15.4067180Z hint:      git config --global init.defaultBranch <name>
2024-03-05T12:15:15.4067974Z hint:
2024-03-05T12:15:15.4068792Z hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
2024-03-05T12:15:15.4070416Z hint: 'development'. The just-created branch can be renamed via this command:
2024-03-05T12:15:15.4071408Z hint:
2024-03-05T12:15:15.4071949Z hint:      git branch -m <name>
2024-03-05T12:15:15.4075546Z Initialized empty Git repository in /home/runner/work/SomeRepo/SomeRepo/.git/
2024-03-05T12:15:15.4088781Z [command]/usr/bin/git remote add origin https://github.com/SomeOwner/SomeRepo
2024-03-05T12:15:15.5198048Z ##[endgroup]
2024-03-05T12:15:15.5199096Z ##[group]Disabling automatic garbage collection
2024-03-05T12:15:15.5200143Z [command]/usr/bin/git config --local gc.auto 0
2024-03-05T12:15:15.5201115Z ##[endgroup]
2024-03-05T12:15:15.5201827Z ##[group]Setting up auth
2024-03-05T12:15:15.5202806Z [command]/usr/bin/git config --local --name-only --get-regexp core\.sshCommand
2024-03-05T12:15:15.5205178Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"
2024-03-05T12:15:15.5207830Z [command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
2024-03-05T12:15:15.5210802Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :"
2024-03-05T12:15:15.5213797Z [command]/usr/bin/git config --local http.https://github.com/.extraheader AUTHORIZATION: basic ***
2024-03-05T12:15:15.5215295Z ##[endgroup]
2024-03-05T12:15:15.5216025Z ##[group]Fetching the repository
2024-03-05T12:15:15.5218447Z [command]/usr/bin/git -c protocol.version=2 fetch --no-tags --prune --progress --no-recurse-submodules --depth=1 origin +333d436a47062b3f68d90522ebd0f8094499110f:refs/remotes/origin/main
2024-03-05T12:15:15.8537720Z remote: Enumerating objects: 8, done.
2024-03-05T12:15:15.8538391Z remote: Counting objects:  12% (1/8)
2024-03-05T12:15:15.8538978Z remote: Counting objects:  25% (2/8)
2024-03-05T12:15:15.8539542Z remote: Counting objects:  37% (3/8)
2024-03-05T12:15:15.8540107Z remote: Counting objects:  50% (4/8)
2024-03-05T12:15:15.8540653Z remote: Counting objects:  62% (5/8)
2024-03-05T12:15:15.8541215Z remote: Counting objects:  75% (6/8)
2024-03-05T12:15:15.8541795Z remote: Counting objects:  87% (7/8)
2024-03-05T12:15:15.8542352Z remote: Counting objects: 100% (8/8)
2024-03-05T12:15:15.8542944Z remote: Counting objects: 100% (8/8), done.
2024-03-05T12:15:15.8543565Z remote: Compressing objects:  20% (1/5)
2024-03-05T12:15:15.8544158Z remote: Compressing objects:  40% (2/5)
2024-03-05T12:15:15.8544754Z remote: Compressing objects:  60% (3/5)
2024-03-05T12:15:15.8545358Z remote: Compressing objects:  80% (4/5)
2024-03-05T12:15:15.8545944Z remote: Compressing objects: 100% (5/5)
2024-03-05T12:15:15.8546570Z remote: Compressing objects: 100% (5/5), done.
2024-03-05T12:15:15.8547619Z remote: Total 8 (delta 0), reused 4 (delta 0), pack-reused 0
2024-03-05T12:15:15.8658809Z From https://github.com/SomeOwner/SomeRepo
2024-03-05T12:15:15.8660050Z  * [new ref]         333d436a47062b3f68d90522ebd0f8094499110f -> origin/main
2024-03-05T12:15:15.8672014Z ##[endgroup]
2024-03-05T12:15:15.8672703Z ##[group]Determining the checkout info
2024-03-05T12:15:15.8674593Z ##[endgroup]
2024-03-05T12:15:15.8675207Z ##[group]Checking out the ref
2024-03-05T12:15:15.8679816Z [command]/usr/bin/git checkout --progress --force -B main refs/remotes/origin/main
2024-03-05T12:15:15.8733130Z Switched to a new branch 'main'
2024-03-05T12:15:15.8734095Z branch 'main' set up to track 'origin/main'.
2024-03-05T12:15:15.8740077Z ##[endgroup]
2024-03-05T12:15:15.8786527Z [command]/usr/bin/git log -1 --format='%H'
2024-03-05T12:15:15.8863482Z '333d436a47062b3f68d90522ebd0f8094499110f'
2024-03-05T12:15:15.9182412Z ##[group]Run git config --local user.email "action@github.com"
2024-03-05T12:15:15.9183302Z git config --local user.email "action@github.com"
2024-03-05T12:15:15.9184027Z git config --local user.name "GitHub Action"
2024-03-05T12:15:15.9226352Z shell: /usr/bin/bash -e
2024-03-05T12:15:15.9226821Z ##[endgroup]
2024-03-05T12:15:15.9480431Z ##[group]Run echo "print(os.getcwd())" > faulty.py
2024-03-05T12:15:15.9481276Z echo "print(os.getcwd())" > faulty.py
2024-03-05T12:15:15.9504474Z shell: /usr/bin/bash -e
2024-03-05T12:15:15.9504914Z ##[endgroup]
2024-03-05T12:15:15.9582268Z ##[group]Run git add faulty.py
2024-03-05T12:15:15.9582757Z git add faulty.py
2024-03-05T12:15:15.9583198Z git commit -m "Add faulty.py"
2024-03-05T12:15:15.9583676Z git push
2024-03-05T12:15:15.9604945Z shell: /usr/bin/bash -e
2024-03-05T12:15:15.9606009Z ##[endgroup]
2024-03-05T12:15:15.9719866Z [main f6d0a35] Add faulty.py
2024-03-05T12:15:15.9720514Z  1 file changed, 1 insertion(+)
2024-03-05T12:15:15.9721063Z  create mode 100644 faulty.py
2024-03-05T12:15:16.6512714Z To https://github.com/SomeOwner/SomeRepo
2024-03-05T12:15:16.6513579Z    333d436..f6d0a35  main -> main
2024-03-05T12:15:16.6546402Z ##[group]Run python faulty.py
2024-03-05T12:15:16.6547081Z python faulty.py
2024-03-05T12:15:16.6574673Z shell: /usr/bin/bash -e
2024-03-05T12:15:16.6575241Z ##[endgroup]
2024-03-05T12:15:16.7905537Z Traceback (most recent call last):
2024-03-05T12:15:16.7906877Z   File "/home/runner/work/SomeRepo/SomeRepo/faulty.py", line 1, in <module>
2024-03-05T12:15:16.7907990Z     print(os.getcwd())
2024-03-05T12:15:16.7908846Z NameError: name 'os' is not defined
2024-03-05T12:15:16.8033229Z ##[error]Process completed with exit code 1.
2024-03-05T12:15:16.8146363Z Post job cleanup.
2024-03-05T12:15:16.9487687Z [command]/usr/bin/git version
2024-03-05T12:15:16.9549525Z git version 2.43.2
2024-03-05T12:15:16.9599494Z Temporarily overriding HOME='/home/runner/work/_temp/f7be9b84-256d-4ad4-91d1-1f56d515e70a' before making global git config changes
2024-03-05T12:15:16.9601538Z Adding repository directory to the temporary git global config as a safe directory
2024-03-05T12:15:16.9604870Z [command]/usr/bin/git config --global --add safe.directory /home/runner/work/SomeRepo/SomeRepo
2024-03-05T12:15:16.9655963Z [command]/usr/bin/git config --local --name-only --get-regexp core\.sshCommand
2024-03-05T12:15:16.9702974Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"
2024-03-05T12:15:16.9992155Z [command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
2024-03-05T12:15:17.0028803Z http.https://github.com/.extraheader
2024-03-05T12:15:17.0042145Z [command]/usr/bin/git config --local --unset-all http.https://github.com/.extraheader
2024-03-05T12:15:17.0090536Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :"
2024-03-05T12:15:17.0813744Z Cleaning up orphan processes

Relevant Information:
2024-03-05T12:15:16.7905537Z Traceback (most recent call last):
2024-03-05T12:15:16.7906877Z   File "/home/runner/work/SomeRepo/SomeRepo/faulty.py", line 1, in <module>
2024-03-05T12:15:16.7907990Z     print(os.getcwd())
2024-03-05T12:15:16.7908846Z NameError: name 'os' is not defined

Summary:
The error is caused by a NameError in the file faulty.py. The import statement for the os module is missing.

Output:
{
  "relevant_infos": '''2024-03-05T12:15:16.7905537Z Traceback (most recent call last):
2024-03-05T12:15:16.7906877Z   File "/home/runner/work/SomeRepo/SomeRepo/faulty.py", line 1, in <module>
2024-03-05T12:15:16.7907990Z     print(os.getcwd())
2024-03-05T12:15:16.7908846Z NameError: name 'os' is not defined''',
  "explanation": "The error is caused by a NameError in the file faulty.py. The import statement for the os module is missing.",
  "files": [
    "faulty.py"
  ]
}

Log:
{log}
"""

repair_prompt = """\
TODO: This is a placeholder for the repair prompt.
"""

commit_prompt = """\
I want you to act as a GitHub commit message generator.
Summarize the following explanations in 3-10 words. The summary should contain \
the most important information from each individual declaration.
Do not write any explanations or other words, just reply with the commit \
message.\n
"""


@dataclass
class Config:
    _instance = None

    def __init__(self):
        ####################
        # Cache CONFIG
        ####################
        self.USE_CACHE = self._read_bool_value("USE_CACHE", "False")

        ####################
        # AGI CONFIG
        ####################
        self.prompts = PromptConfig()
        self.AGI_VERBOSE = True
        self.LLM_MODEL_NAME = os.environ.get("LLM_MODEL_NAME", "gpt-3.5-turbo-1106")
        self.LLM_TEMPERATURE = os.environ.get("LLM_TEMPERATURE", 0.0)
        self.LLM_MAX_LENGTH = os.environ.get("LLM_MAX_LENGTH", 512)

        #######################
        # AZURE OPENAI CONFIG
        #######################
        self.OPENAI_API_BASE = os.environ.get("OPENAI_API_BASE")
        self.OPENAI_DEPLOYMENT_NAME = os.environ.get("OPENAI_DEPLOYMENT_NAME")
        self.OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
        self.OPENAI_API_VERSION = os.environ.get("OPENAI_API_VERSION", "2023-05-15")
        self.OPENAI_API_TYPE = os.environ.get("OPENAI_API_TYPE", "azure")

        ####################
        # WORKING DIR CONFIG
        ####################

        if os.environ.get("WORKING_DIR"):
            self.WORKING_DIR = os.environ.get("WORKING_DIR")
        else:
            temp_dir = os.path.join(tempfile.gettempdir(), "cdaas-merge")
            os.makedirs(temp_dir, exist_ok=True)
            self.WORKING_DIR = temp_dir
        LOGGER.info("Working directory: %s", self.WORKING_DIR)

    def _read_bool_value(self, env_name, default_value: bool) -> bool:
        """
        Read a boolean value from an environment variable.
        Args:
            env_value (str): The environment variable value.
        Returns:
            bool: The boolean value.
        """
        env_value: str | bool = os.environ.get(env_name, default_value)
        if env_value is None:
            return default_value

        if isinstance(env_value, bool):
            return env_value
        return env_value.lower() in ["true", "1"]

    @classmethod
    def instance(cls):
        """Create a singleton instance of the Config class.
        Returns:
            Config: The singleton instance of the Config class.
        """
        if cls._instance is None:
            logging.info("Creating new Config instance")
            cls._instance = Config()
            # cls._instance.validate_github_user()
            # cls._instance.validate_llm_setup()
            # Put any initialization here.
        return cls._instance

    def validate_llm_setup(self):
        """Validate the LLM setup.
        This function checks if all required environment variables are set.

        Raises:
            SystemExit: If any required environment variable is not set.
        """
        if not self.OPENAI_API_BASE:
            sys.stderr.write(
                "ERROR: OPENAI_API_BASE is not set. Please check your environment variables."
            )
            sys.exit(3)

        if not self.OPENAI_DEPLOYMENT_NAME:
            sys.stderr.write(
                "ERROR: OPENAI_DEPLOYMENT_NAME is not set. Please check your environment variables."
            )
            sys.exit(3)

        if not self.OPENAI_API_KEY:
            sys.stderr.write(
                "ERROR: OPENAI_API_KEY is not set. Please check your environment variables."
            )
            sys.exit(3)

        if not self.OPENAI_API_TYPE:
            sys.stderr.write(
                "ERROR: OPENAI_API_TYPE is not set. Please check your environment variables."
            )
            sys.exit(3)


def load_config():
    return Config.instance()
