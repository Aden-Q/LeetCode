class Solution:
    def minCost(self, n: int, roads: List[List[int]], appleCost: List[int], k: int) -> List[int]:
        graph = [[] for _ in range(n)]

        for city_a, city_b, cost in roads:
            graph[city_a-1].append((city_b-1, cost))
            graph[city_b-1].append((city_a-1, cost))

        res = list(appleCost)

        heap = [(apple_cost, start_city) for start_city, apple_cost in enumerate(appleCost)]

        while heap:
            total_cost, cur_city = heapq.heappop(heap)

            if res[cur_city] < total_cost:
                continue

            for next_city, cost in graph[cur_city]:
                if res[next_city] > res[cur_city] + (k + 1) * cost:
                    res[next_city] = res[cur_city] + (k + 1) * cost
                    heapq.heappush(heap, (res[next_city], next_city))

        return res
