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


if __name__ == '__main__':
    unittest.main()
