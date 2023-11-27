class TrieNode: 
    def __init__(self):
        self.children: dict[str, TrieNode] = {}
        self.is_terminal = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        """Insert a word into the Trie.

        Args:
            word (str): character list representing the word to add in the structure.
        """
        pass

    def search(self, word: str) -> bool:
        """Search if the word exists in that Trie.

        Args:
            word (str): character list representing the word to search in the structure.

        Returns:
            bool: True if the word argument was found in the Trie, otherwise return False.
        """
        pass

    def starts_with(self, prefix: str) -> bool:
        """Check if there is any word in the Trie that starts with the given prefix. 

        Args:
            prefix (str): character list representing the prefix to search in the structure.

        Returns:
            bool: True if the prefix argument was found in the Trie, otherwise return False.
        """
        pass