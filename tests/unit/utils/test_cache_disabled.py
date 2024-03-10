import pytest
from src.utils.cache import DisabledCache


@pytest.fixture
def cache():
    c = DisabledCache(tmp_path="./tmp/")
    yield c


def test_update(cache):
    prompt = "test_prompt"
    answer = "test_answer"
    assert cache.update(prompt, answer) == False


def test_lookup(cache):
    prompt = "test_prompt"
    answer = "test_answer"
    assert not cache.lookup(prompt)
    cache.update(prompt, answer)
    assert not cache.lookup(prompt)


def test_get_answer(cache):
    prompt = "test_prompt"
    answer = "test_answer"
    assert cache.get_answer(prompt) is None
    cache.update(prompt, answer)
    assert cache.get_answer(prompt) is None
