import unittest

from src.data_structures.hashset.hashset import HashSet

class TestHashSet(unittest.TestCase):
    def test_add_and_contains(self):
        hash_set = HashSet()
        hash_set.add(1)
        self.assertTrue(hash_set.contains(1))
    
    def test_remove(self):
        hash_set = HashSet()
        hash_set.add(1)
        hash_set.remove(1)
        self.assertFalse(hash_set.contains(1))
    
    def test_contains_empty_set(self):
        hash_set = HashSet()
        self.assertFalse(hash_set.contains(1))
    
    def test_contains_non_existing_element(self):
        hash_set = HashSet()
        hash_set.add(2)
        self.assertFalse(hash_set.contains(1))

if __name__ == '__main__':
    unittest.main()