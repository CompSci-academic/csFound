class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# Create a Trie
trie = Trie()

# Insert words into the Trie
trie.insert("apple")
trie.insert("app")
trie.insert("banana")
trie.insert("bat")
trie.insert("ball")

# Search for words in the Trie
print("Is 'apple' in the Trie?", trie.search("apple"))
print("Is 'app' in the Trie?", trie.search("app"))
print("Is 'orange' in the Trie?", trie.search("orange"))

# Check if words with a common prefix exist
print("Does any word start with 'ba'?", trie.starts_with("ba"))
print("Does any word start with 'abc'?", trie.starts_with("abc"))
