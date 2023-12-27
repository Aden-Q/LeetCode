class TrieNode:
    def __init__(self):
        self.isEnd = False
        # we have at most 26 children using alphabet
        self.children = [None] * 26

class Trie:
    def __init__(self):
        self.trie = TrieNode()

    def insert(self, word) -> None:
        node = self.trie
        for c in word:
            idx = ord(c) - 97
            if not node.children[idx]:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.isEnd = True

    # search a prefix in the tree
    def searchPrefix(self, prefix) -> TrieNode:
        node = self.trie
        for c in prefix:
            idx = ord(c) - 97
            if not node.children[idx]:
                return None
            node = node.children[idx]
        return node

    # the current path in the recursive call
    # dfs starts searching at node
    def dfs(self, node: TrieNode, path: List[str]) -> None:
        if not node:
            return
        if len(self.buffer) == 3:
            return
        if node.isEnd:
            # we've found a path
            self.buffer.append(''.join(path))
        
        for child in string.ascii_lowercase:
            idx = ord(child) - 97
            if node.children[idx]:
                path.append(child)
                self.dfs(node.children[idx], path)
                path.pop()

        return

    def getWordsStartingWith(self, prefix) -> List[str]:
        prefix_node = self.searchPrefix(prefix)
        # we need to result to avoid successive calls producing inconsistent results
        self.buffer = []
        # we pass in path as a list of characters because list operation is O(1)
        self.dfs(prefix_node, [c for c in prefix])
        return self.buffer

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for product in products:
            trie.insert(product)

        ans = []
        prefix = ""
        for c in searchWord:
            prefix += c
            # next we need to find three lexicographically minimum products that have a common prefix with the given prefix
            ans.append(trie.getWordsStartingWith(prefix))

        return ans
