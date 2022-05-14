class TrieNode:
    def __init__(self, val = None):
        self.val = val
        self.children = [None] * 256

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.size = 0
        
    def getNode(self, node, key: str) -> TrieNode:
        p = node
        for c in key:
            if not p:
                return p
            p = p.children[ord(c)]
        return p

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if not node.children[ord(c)]:
                node.children[ord(c)] = TrieNode()
            node = node.children[ord(c)]
        node.val = 1

    def search(self, word: str) -> bool:
        node = self.getNode(self.root, word)
        if not node or not node.val:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        node = self.getNode(self.root, prefix)
        if not node:
            return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)