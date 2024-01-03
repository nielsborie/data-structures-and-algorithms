class TrieNode: 
    def __init__(self):
        self.children: dict[str, TrieNode | None] = {}
        self.is_terminal = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        """Insert a word into the Trie in a case-insensitive manner.

        Args:
            word (str): String representing the word to add in the structure.
        """
        current_node = self.root
        word = word.lower() # Convert the word to lowercase
        for character in word:
            if character not in current_node.children:
                current_node.children[character] = TrieNode()
            current_node = current_node.children[character]
        current_node.is_terminal = True


    def search(self, word: str) -> bool:
        """Search if the word exists in that Trie in a case-insensitive manner.

        Args:
            word (str): String representing the word to search in the structure.

        Returns:
            bool: True if the word argument was found in the Trie, otherwise return False.
        """
        if not self.root:
            return False
        
        current_node = self.root
        word = word.lower() # Convert the word to lowercase
        for character in word:
            if character not in current_node.children:
                return False
            current_node = current_node.children[character]
        return current_node.is_terminal if current_node is not None else False

    def starts_with(self, prefix: str) -> bool:
        """Check if there is any word in the Trie that starts with the given prefix in a case-insensitive manner.

        Args:
            prefix (str): String representing the prefix to search in the structure.

        Returns:
            bool: True if the prefix argument was found in the Trie, otherwise return False.
        """
        current_node = self.root
        prefix = prefix.lower()  # Convert the prefix to lowercase
        for character in prefix:
            if character not in current_node.children:
                return False
            current_node = current_node.children[character]
        return current_node is not None
    
    def remove(self, key: str) -> None:
        key = key.lower()
        self.root = self._remove(self.root, key, 0)

    def _remove(self, node: TrieNode, key: str, depth: int) -> TrieNode:
        # Base case: if the node is None, the key is not present
        if node is None:
            return None

        # Base case: we have reached the end of the key
        if depth == len(key):
            # If the node is terminal, mark it as non-terminal
            if node.is_terminal:
                node.is_terminal = False
            # If the node has no children after removal, return None to update the parent's reference
            if not node.children:
                return None
            # Otherwise, return the node as is
            return node

        # Get the current character from the key
        char = key[depth]

        # Check if the character is present in the node's children
        if char not in node.children:
            # The character is not present, the key does not exist in the Trie
            return node

        # Recursively, call _remove to remove the rest of the key
        child = node.children[char]
        node.children[char] = self._remove(child, key, depth + 1)

        # If the current node is not a terminal node and has no children after removal, return None
        if not node.is_terminal and not any(node.children.values()):
            return None

        # Otherwise, return the updated node
        return node
    
if __name__ == "__main__":
    trie = Trie()
    word_to_insert = "apple"

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

    print(f"- Deleting {word_to_insert=} from our Trie...")
    trie.remove(word_to_insert)
    print(f"? Checking if {word_to_insert=} exists in that Trie -> {trie.search(word_to_insert)=}")