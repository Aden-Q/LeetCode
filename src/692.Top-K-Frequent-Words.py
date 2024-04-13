class Node:
    def __init__(self, word, cnt):
        self.word = word
        self.cnt = cnt

    def __lt__(self, other):
        return self.cnt < other.cnt or (self.cnt == other.cnt and self.word > other.word)

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = collections.Counter(words)

        # we want a min heap, containing k most frequent words
        heap = []
        for word, cnt in d.items():
            heapq.heappush(heap, Node(word, cnt))
            if len(heap) > k:
                heapq.heappop(heap)

        res = deque()
        while heap:
            res.appendleft(heapq.heappop(heap).word)

        return res
