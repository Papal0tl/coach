"""
Tests for LRU Cache.
"""

from agent_solution import LRUCache


def test_examples():
    cache = LRUCache(2)
    assert cache is not None


if __name__ == "__main__":
    test_examples()
