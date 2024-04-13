class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0:
            return s

        counter = Counter(s)
        pq = [(-v, k) for k, v in counter.items()]
        heapq.heapify(pq)
        res = ""

        while pq:
            if len(pq) < k and -pq[0][0] > 1:
                return ''

            queue = []
            size = len(pq)
            # otherwise we append k characters to it
            for _ in range(min(size, k)):
                curr_node = heapq.heappop(pq)
                if -curr_node[0] > 1:
                    queue.append(curr_node)
                res += curr_node[1]

            for node in queue:
                heapq.heappush(pq, (node[0]+1, node[1]))

        return res
