import unittest

from src.data_structures.linked_list.linked_list import LinkedList

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.linked_list = LinkedList()

    def test_append_and_display(self):
        # Given
        expected_output = [1, 2, 3, 4]

        # When
        self.linked_list.append(1)
        self.linked_list.append(2)
        self.linked_list.append(3)
        self.linked_list.append(4)

        # Then
        self.assertEqual(self.linked_list.display(), expected_output)

    def test_get_valid_index(self):
        # Given
        expected_value = 3

        # When
        self.linked_list.append(1)
        self.linked_list.append(2)
        self.linked_list.append(3)

        # Then
        self.assertEqual(self.linked_list.get(2), expected_value)

    def test_get_invalid_index(self):
        # Given

        # When
        self.linked_list.append(1)
        
        # Then
        self.assertEqual(self.linked_list.get(0), 1)
        with self.assertRaises(IndexError):
            self.linked_list.get(1)

    def test_delete_valid_index(self):
        # Given
        expected_output = [1, 2, 4]

        # When
        self.linked_list.append(1)
        self.linked_list.append(2)
        self.linked_list.append(3)
        self.linked_list.append(4)
        
        # Then
        self.linked_list.delete(2)
        self.assertEqual(self.linked_list.display(), expected_output)

    def test_delete_invalid_index(self):
         # Given

         # When
         self.linked_list.append(1)

         # Then
         with self.assertRaises(IndexError):
             self.linked_list.delete(1)

if __name__ == '__main__':
    unittest.main()