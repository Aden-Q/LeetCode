class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n+1)]
        for edge in times:
            start, end, weight = edge
            graph[start].append((end, weight))

        dist = [float('inf')] * (n+1)
        dist[k] = 0
        # store pairs of (dist, node_id)
        pq = [(0, k)]
        while pq:
            curr_node_dist, curr_node_id = heapq.heappop(pq)
            if curr_node_dist > dist[curr_node_id]:
                continue
            # otherwise we relax edges
            for next_node_id, weight in graph[curr_node_id]:
                next_dist = curr_node_dist + weight
                if next_dist >= dist[next_node_id]:
                    continue
                dist[next_node_id] = next_dist
                heapq.heappush(pq, (next_dist, next_node_id))

        ans = max(dist[1:])
        return ans if ans != float('inf') else -1
