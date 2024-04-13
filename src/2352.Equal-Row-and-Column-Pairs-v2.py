class TrieNode:
    def __init__(self):
        self.count = 0
        self.children = {}

class Trie:
    def __init__(self):
        self.trie = TrieNode()

    def insert(self, prefix):
        curr = self.trie
        for c in prefix:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        
        curr.count += 1

    def search(self, prefix) -> int:
        curr = self.trie
        for c in prefix:
            if c not in curr.children:
                return 0
            curr = curr.children[c]
        
        return curr.count

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        trie = Trie()
        
        for row in grid:
            trie.insert(row)

        res = 0
        for col_idx in range(n):
            col = [grid[row][col_idx] for row in range(n)]
            res += trie.search(col)

        return res
