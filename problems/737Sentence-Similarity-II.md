# 737. Sentence Similarity II
**Difficulty:** Medium

## URL

https://leetcode.com/problems/sentence-similarity-ii/

## Solution

### Approach 1: Union-Find

```python
class UF:
    def __init__(self, n):
        self.parent = list(range(n))
        
    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]
    
    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)
        self.parent[root_p] = root_q
        return
    
    def connected(self, p, q):
        return self.find(p) == self.find(q)

class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        ht = {}
        word_id = 0
        for pair in similarPairs:
            if pair[0] not in ht:
                ht[pair[0]] = word_id
                word_id += 1
            if pair[1] not in ht:
                ht[pair[1]] = word_id
                word_id += 1
        for word in sentence1:
            if word not in ht:
                ht[word] = word_id
                word_id += 1
        for word in sentence2:
            if word not in ht:
                ht[word] = word_id
                word_id += 1
        
        uf = UF(word_id)
        for pair in similarPairs:
            op1 = ht[pair[0]]
            op2 = ht[pair[1]]
            uf.union(op1, op2)
        for i in range(len(sentence1)):
            if not uf.connected(ht[sentence1[i]], ht[sentence2[i]]):
                return False
        return True
```

