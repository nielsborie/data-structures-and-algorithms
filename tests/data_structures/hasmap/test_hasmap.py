import unittest

from src.data_structures.hashmap.hashmap import HashMap


class TestHashMap(unittest.TestCase):
    def test_put(self):
        # Given
        hash_map = HashMap()

        # When
        hash_map.put(1, 1)
        hash_map.put(1000, 2)
        hash_map.put(12, 45)

        # Then
        self.assertEqual(hash_map.get(1), 1)
        self.assertEqual(hash_map.get(1000), 2)
        self.assertEqual(hash_map.get(12), 45)
        self.assertEqual(hash_map.get(11), -1)

    def test_delete(self):
        # Given
        hash_map = HashMap()
        hash_map.put(1, 1)
        hash_map.put(1000, 2)

        # When
        hash_map.delete(1)

        # Then
        self.assertEqual(hash_map.get(1), -1)
        self.assertEqual(hash_map.get(1000), 2)

    def test_contains(self):
        # Given
        hash_map = HashMap()
        hash_map.put(1, 1)

        # Then
        self.assertTrue(hash_map.contains(1))
        self.assertFalse(hash_map.contains(2))

    def test_get_size_with_single_value(self):
        # Given
        hash_map = HashMap()
        
        # When
        hash_map.put(1, 1)
        
        # Then
        self.assertEqual(hash_map.get_size(), 1)
        
    def test_get_size(self):
        # Given
        hash_map = HashMap()
        
        # When
        hash_map.put(1, 1)
        hash_map.put(2, 1)
        hash_map.put(3, 1)
        hash_map.put(4, 1)
        hash_map.put(5, 1)
        
        # Then
        self.assertEqual(hash_map.get_size(), 5)