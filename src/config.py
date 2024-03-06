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

log_prompt = """
You will receive the log of a failed CI/CD pipeline. The log contains \
unnecessary information. You'll be given a workflow to follow along with some \
examples:
1. Search for the relevant information that describes the cause of the error.
2. Identify the file in which the error is caused and which need to be \
corrected.
3. Return a Json file with the keys "explanation", "error_area" and "file".
The cause of the error (str), as described in 1., should be in "Explanation".
The lines of code that are causing the error (str), should be in "error_area".
The file (str) that caused the error should be in "file".

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
        self.LLM_MODEL_NAME = os.environ.get("LLM_MODEL_NAME", "gpt-4-1106-preview")
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
