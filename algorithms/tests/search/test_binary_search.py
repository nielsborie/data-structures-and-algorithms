import unittest

from algorithms.search.binary_search import BinarySearchIterativeVersion, BinarySearchRecursiveVersion


class BaseBinarySearchTest(unittest.TestCase):
    def setUp(self):
        self.search_class = None
        self.skip_test = True

    def test_binary_search_present(self):
        test_cases = [
            ([1, 2, 3, 4, 5], 4, 3),
            ([1, 3, 5, 7, 9], 3, 1),
            ([1, 3, 5, 7, 9], 1, 0),
            ([1, 3, 5, 7, 9], 9, 4),
        ]
        self.run_test_cases(test_cases)

    def test_binary_search_not_present(self):
        test_cases = [
            ([1, 2, 3, 4, 5], 6, -1),
            ([], 10, -1),
            ([2], 10, -1),
            ([1, 3, 5, 7, 9], 8, -1),
        ]
        self.run_test_cases(test_cases)

    def test_binary_search_edge_cases(self):
        test_cases = [
            ([1], 1, 0),
            ([1, 2], 2, 1),
        ]
        self.run_test_cases(test_cases)

    def run_test_cases(self, test_cases):
        if not self.skip_test:
            for arr, target, expected in test_cases:
                with self.subTest(arr=arr, target=target):
                    searcher = self.search_class()
                    self.assertEqual(searcher.binary_search(arr, target), expected)
        else: 
            self.skipTest("Tests are not activated for this class.")

class BinarySearchClass1Test(BaseBinarySearchTest):
    def setUp(self):
        self.search_class = BinarySearchIterativeVersion
        self.skip_test = False

class BinarySearchClass2Test(BaseBinarySearchTest):
    def setUp(self):
        self.search_class = BinarySearchRecursiveVersion
        self.skip_test = False

if __name__ == '__main__':
    if __name__ == '__main__' and __package__ is None:
        loader = unittest.TestLoader()
        suite = unittest.TestSuite()
        for subclass in BaseBinarySearchTest.__subclasses__():
            suite.addTests(loader.loadTestsFromTestCase(subclass) if subclass.__name__ != 'BaseBinarySearchTest' else unittest.TestSuite())
        unittest.TextTestRunner(verbosity=2).run(suite)