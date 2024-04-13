class TrieNode:
    def __init__(self, val = None):
        self.val = val
        self.children = [None] * 26

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        p = self.root
        for c in word:
            offset_c = ord(c) - 97
            if not p.children[offset_c]:
                p.children[offset_c] = TrieNode()
            p = p.children[offset_c]
        p.val = 1

    def hasKeyWithPattern(self, node, key, start):
        if not node:
            return False
        if start >= len(key):
            if node.val:
                return True
            return False
        c = key[start]
        if c != '.':
            return self.hasKeyWithPattern(node.children[ord(c) - 97], key, start + 1)
        for i in range(26):
            if (self.hasKeyWithPattern(node.children[i], key, start + 1)):
                return True
        return False
    
    def search(self, word: str) -> bool:
        return self.hasKeyWithPattern(self.root, word, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)