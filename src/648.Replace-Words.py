class TrieNode:
    def __init__(self, val = None):
        self.val = val
        self.children = [None] * 26
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.size = 0
        
    def getNode(self, key):
        p = self.root
        for c in key:
            if not p:
                return p
            p = p.children[ord(c) - 97]
        return p
    
    def insert(self, key):
        p = self.root
        for c in key:
            if not p.children[ord(c) - 97]:
                p.children[ord(c) - 97] = TrieNode()
            p = p.children[ord(c) - 97]
        p.val = 1
        
    def shortestPrefix(self, key):
        p = self.root
        for i in range(len(key)):
            if not p:
                return ''
            if p.val:
                return key[: i]
            c = key[i]
            p = p.children[ord(c) - 97]
        if p and p.val:
            return key
        return ''

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        res = []
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        for word in sentence.split():
            st_prefix = trie.shortestPrefix(word)
            if st_prefix:
                res.append(st_prefix)
            else:
                res.append(word)
        return ' '.join(res)