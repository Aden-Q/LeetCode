class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        heap_map = defaultdict(list)
        for id, score in items:
            heapq.heappush(heap_map[id], score)
            if len(heap_map[id]) > 5:
                heapq.heappop(heap_map[id])
        
        res = []
        for id in sorted(heap_map.keys()):
            res.append([id, sum(heap_map[id]) // 5])

        return res
