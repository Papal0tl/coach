"""
Tests for LRU Cache.
"""

from agent_solution import LRUCache


def test_example_from_problem():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)          # evicts key 2
    assert cache.get(2) == -1
    cache.put(4, 4)          # evicts key 1
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4


def test_capacity_one():
    cache = LRUCache(1)
    cache.put(1, 1)
    assert cache.get(1) == 1
    cache.put(2, 2)          # evicts key 1
    assert cache.get(1) == -1
    assert cache.get(2) == 2


def test_get_missing_key():
    cache = LRUCache(2)
    assert cache.get(1) == -1


def test_put_updates_existing_key_and_recency():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(1, 10)         # update value, 1 becomes most recently used
    cache.put(3, 3)          # evicts key 2, not key 1
    assert cache.get(1) == 10
    assert cache.get(2) == -1
    assert cache.get(3) == 3


def test_get_refreshes_recency():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)              # 1 becomes most recently used
    cache.put(3, 3)           # evicts key 2, not key 1
    assert cache.get(2) == -1
    assert cache.get(1) == 1
    assert cache.get(3) == 3


def test_eviction_at_exact_capacity_boundary():
    cache = LRUCache(3)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(3, 3)
    assert cache.get(1) == 1
    assert cache.get(2) == 2
    assert cache.get(3) == 3
    cache.put(4, 4)            # cache full, evicts key 1 (least recently used)
    assert cache.get(1) == -1
    assert cache.get(2) == 2
    assert cache.get(3) == 3
    assert cache.get(4) == 4


if __name__ == "__main__":
    test_example_from_problem()
    test_capacity_one()
    test_get_missing_key()
    test_put_updates_existing_key_and_recency()
    test_get_refreshes_recency()
    test_eviction_at_exact_capacity_boundary()
    print("All tests passed.")
