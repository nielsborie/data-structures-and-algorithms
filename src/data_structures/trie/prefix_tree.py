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
        current_node = self.root
        for character in word:
            if character not in current_node.children:
                current_node.children[character] = TrieNode()
            current_node = current_node.children[character]
        current_node.is_terminal = True


    def search(self, word: str) -> bool:
        """Search if the word exists in that Trie.

        Args:
            word (str): character list representing the word to search in the structure.

        Returns:
            bool: True if the word argument was found in the Trie, otherwise return False.
        """
        current_node = self.root
        for character in word:
            if character not in current_node.children:
                return False
            current_node = current_node.children[character]
        return current_node.is_terminal

    def starts_with(self, prefix: str) -> bool:
        """Check if there is any word in the Trie that starts with the given prefix. 

        Args:
            prefix (str): character list representing the prefix to search in the structure.

        Returns:
            bool: True if the prefix argument was found in the Trie, otherwise return False.
        """
        current_node = self.root
        for character in prefix:
            if character not in current_node.children:
                return False
            current_node = current_node.children[character]
        return True


if __name__ == "__main__":
    trie = Trie()
    word_to_insert = "apple"
    trie.insert(word_to_insert)
    assert trie.search(word_to_insert), f"{word_to_insert=} doesn't exist in that Trie."

    print(f"- Inserting {word_to_insert=} into our Trie...")
    trie.insert(word_to_insert)
    print(f"? Checking if {word_to_insert=} exists in that Trie -> {trie.search(word_to_insert)=}")
    non_existing_word = "a"
    print(f"? Checking if {non_existing_word=} exists in that Trie -> {trie.search(non_existing_word)=}")
    print(f"? Checking if {non_existing_word=} is a correct 'prefix' in that Trie -> {trie.starts_with(non_existing_word)=}")
    valid_prefix = "ap"
    print(f"? Checking if {valid_prefix=} is a correct 'prefix' in that Trie -> {trie.starts_with(valid_prefix)=}")
    invalid_prefix = "apd"
    print(f"? Checking if {invalid_prefix=} is a correct 'prefix' in that Trie -> {trie.starts_with(invalid_prefix)=}")