from sortedcontainers import SortedList

class TrieNode:
    def __init__(self):
        self.len_idx = SortedList()
        self.children = [None] * 26

class Trie:
    def __init__(self):
        self.trie = TrieNode()

    def insert(self, word: str, index: int) -> None:
        node = self.trie
        for c in word:
            idx = ord(c) - ord('a')
            if not node.children[idx]:
                node.children[idx] = TrieNode()
            node.children[idx].len_idx.add((len(word), index))
            node = node.children[idx]

    def search(self, word: str) -> []:
        ans = []
        node = self.trie
        for c in word:
            idx = ord(c) - ord('a')
            if not node.children[idx]:
                return ans
            node = node.children[idx]
            ans = node.len_idx

        return ans

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        global_optimal = [(len(word), idx) for idx, word in enumerate(wordsContainer)]
        global_optimal.sort()
        optimal = global_optimal[0][1]

        trie = Trie()
        n = len(wordsQuery)
        ans = [0] * n
        for idx, word in enumerate(wordsContainer):
            rev_word = word[::-1]
            trie.insert(rev_word, idx)
            
        for i in range(n):
            rev_w = wordsQuery[i][::-1]
            res = trie.search(rev_w)
            ans[i] = res[0][1] if res else optimal
            
        return ans
