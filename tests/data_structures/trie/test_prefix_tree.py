import unittest

from src.data_structures.trie.prefix_tree import Trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()

    def test_insert_and_search(self):
        # Given
        words = ["apple", "banana", "app", "bat"]
        for word in words:
            self.trie.insert(word)

        # When/Then
        for word in words:
            with self.subTest(word=word):
                # When
                result = self.trie.search(word)

                # Then
                self.assertTrue(result, f"Failed to find {word} after insertion")

        # When/Then
        non_existing_words = ["orange", "apples", "batman"]
        for word in non_existing_words:
            with self.subTest(word=word):
                # When
                result = self.trie.search(word)

                # Then
                self.assertFalse(result, f"Incorrectly found {word}")

    def test_starts_with(self):
        # Given
        prefixes = ["app", "ban", "ba", "bat"]
        for prefix in prefixes:
            self.trie.insert(prefix + "le")

        # When/Then
        for prefix in prefixes:
            with self.subTest(prefix=prefix):
                # When
                result = self.trie.starts_with(prefix)

                # Then
                expected_result = any(word.startswith(prefix) for word in ["apple", "banana", "app", "bat"])
                self.assertEqual(result, expected_result, f"Incorrectly found prefix {prefix}")

        # When/Then
        non_existing_prefixes = ["ora", "appe", "batm"]
        for prefix in non_existing_prefixes:
            with self.subTest(prefix=prefix):
                # When
                result = self.trie.starts_with(prefix)

                # Then
                self.assertFalse(result, f"Incorrectly found prefix {prefix}")


    def test_case_insensitivity(self):
        # Given
        words = ["Apple", "Banana", "apPle", "BaT"]
        for word in words:
            self.trie.insert(word)

        # When/Then
        for word in words:
            with self.subTest(word=word):
                # When
                result_lower = self.trie.search(word.lower())
                result_upper = self.trie.search(word.upper())

                # Then
                self.assertTrue(result_lower, f"Failed to find {word} in a case-insensitive manner (lowercase)")
                self.assertTrue(result_upper, f"Failed to find {word} in a case-insensitive manner (uppercase)")

    def test_empty_string(self):
        # Given
        self.trie.insert("")

        # When/Then
        # Test inserting and searching an empty string
        result_empty = self.trie.search("")
        result_prefix_empty = self.trie.starts_with("")

        # Then
        self.assertTrue(result_empty, "Failed to find empty string")
        self.assertTrue(result_prefix_empty, "Failed to find empty string as a prefix")

    def test_repeated_insertion(self):
        # Given
        word = "apple"
        self.trie.insert(word)

        # When/Then
        # Test inserting the same word again
        result_initial_insertion = self.trie.search(word)

        # When
        self.trie.insert(word)

        # Then
        result_repeated_insertion = self.trie.search(word)

        # Then
        self.assertTrue(result_initial_insertion, "Failed to find word after initial insertion")
        self.assertTrue(result_repeated_insertion, "Failed to find word after repeated insertion")
    
    def test_remove_words(self):
        # Given
        words = ["apple", "apples", "banana", "bananas"]
        for word in words:
            self.trie.insert(word)

        # When/Then
        self.trie.remove("apple")
        self.assertFalse(self.trie.search("apple"), f"Incorrectly found 'apple'")
        self.assertTrue(self.trie.search("apples"), f"Failed to find 'apples' after insertion")

        self.trie.remove("bananas")
        self.assertFalse(self.trie.search("bananas"), f"Incorrectly found 'bananas'")
        self.assertTrue(self.trie.search("banana"), f"Failed to find 'banana' after insertion")

    def test_suggestions(self):
        # Given
        trie = Trie()
        words = ["apple", "apples", "banana", "bananas", "Bartender"]
        for word in words:
            trie.insert(word)

        # When 
        a_suggestion = trie.suggest("ap")
        b_suggestion = trie.suggest("b")
        c_suggestion = trie.suggest("c")

        # Then
        self.assertListEqual(a_suggestion, ["apple", "apples"])
        self.assertListEqual(b_suggestion, ["banana", "bananas", "bartender"])
        self.assertIsNone(c_suggestion)
    
    
        

if __name__ == '__main__':
    unittest.main()
