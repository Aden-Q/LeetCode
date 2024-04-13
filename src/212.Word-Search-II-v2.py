class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = {}
        # only se when self.isEnd is true, the full word on this path
        self.word = ""

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # insert a word into the trie
    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        
        # mark this node to say this a word branch
        curr.isEnd = True
        # write down the full word so we don't have to build it backwards
        curr.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # first we build a trie from words
        trie = Trie()
        for word in words:
            trie.insert(word)

        # now we run bfs on the board to search words
        res = set()
        m, n= len(board), len(board[0])
        # we do not want to reuse the same char twice
        visited = [[False] * n for _ in range(m)]
        # node is the parent node in the trie
        def dfs(row, col, node):
            nonlocal res, board
            currChar = board[row][col]
            if board[row][col] not in node.children:
                return
            
            visited[row][col] = True
            if node.children[currChar].isEnd:
                # we find a word
                res.add(node.children[currChar].word)

            # check all neighbors
            for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                next_row, next_col = row + dx, col + dy
                if next_row < 0 or next_row >= m or next_col < 0 or next_col >= n or visited[next_row][next_col]:
                    continue
                dfs(next_row, next_col, node.children[currChar])

            if not node.children[currChar]:
                node.children.pop(currChar)
            visited[row][col] = False
        
        for row in range(m):
            for col in range(n):
                dfs(row, col, trie.root)

        return list(res)
