from collections import Counter
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:        
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        q = deque([beginWord])
        step = 0
        wordList.discard(beginWord)
        while len(q) != 0:
            sz = len(q)
            step += 1
            for _ in range(sz):
                cur_node = q.popleft()
                if cur_node == endWord:
                    return step
                for i in range(len(cur_node)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        next_node = cur_node[:i] + c + cur_node[i+1:]
                        if next_node in wordList:
                            wordList.remove(next_node)
                            q.append(next_node)
        return 0