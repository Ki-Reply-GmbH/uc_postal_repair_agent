import ast
import json
import logging

import openai

from config import Config
from utils.cache import Cache
from utils.functions import decode_from_base64, encode_to_base64

LOGGER = logging.getLogger(__name__)


class LLModel:
    def __init__(self, config: Config, cache: Cache = None):
        openai.api_key = config.OPENAI_API_KEY
        self._cache = cache
        self._model_name = config.LLM_MODEL_NAME
        self._temperature = config.LLM_TEMPERATURE

    def _get_llm_completion(self, prompt, resp_fmt_type="text"):
        """
        Sends a prompt to the OpenAI API and returns the AI's response.
        """
        messages = [
            {
                "role": "system",
                "content": "You are a system designed to solve GitHub merge conflicts.",
            },
            {"role": "user", "content": prompt},
        ]
        response = openai.OpenAI().chat.completions.create(
            model=self._model_name,
            messages=messages,
            temperature=self._temperature,  # this is the degree of randomness of the model's output,
            response_format={"type": resp_fmt_type},
        )
        return response.choices[0].message.content

    def get_completion(self, prompt, resp_fmt_type: str = "json_object"):
        LOGGER.debug("Getting completion for prompt: %s", prompt)
        base64_prompt = encode_to_base64(prompt)

        if resp_fmt_type == "json_object":
            return self._get_completion_json(prompt, base64_prompt)

        return self._get_completion_text(prompt, base64_prompt)

    def _get_completion_json(self, prompt, base64_prompt: str):
        if self._cache.lookup(base64_prompt):
            cache_content = self._cache.get_answer(base64_prompt)
            response = decode_from_base64(cache_content)
            # Prevent json.loads from throwing an error
            response = ast.literal_eval(response)
        else:
            response = json.loads(self._get_llm_completion(prompt, "json_object"))
            self._cache.update(base64_prompt, encode_to_base64(response))

        return response

    def _get_completion_text(self, prompt, base64_prompt: str):
        if self._cache.lookup(base64_prompt):
            cache_content = self._cache.get_answer(base64_prompt)
            response = decode_from_base64(cache_content)
        else:
            response = self._get_llm_completion(prompt, "text")
            self._cache.update(base64_prompt, encode_to_base64(response))

        return response
