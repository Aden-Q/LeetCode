class Solution:
    def placedCoins(self, edges: List[List[int]], cost: List[int]) -> List[int]:
        n = len(cost)
        coin = [0] * n

        # build the graph first
        graph = [[] for _ in range(n)]
        for first, second in edges:
            graph[first].append(second)
            graph[second].append(first)

        # post order traversal
        # for each node, returns a sorted list of cost for the subtree rooted at node
        # containing 5 elements: the largest 3 cost + the smalles 2 cost
        def dfs(node, parent) -> (int, List[int], List[int]):
            nonlocal coin

            # we use a min heap for positive nums and a max heap for negative nums
            # this way we can ensure there's no overlaps
            # minHeap of size 3, only stores positive cost
            posHeap = []
            # maxHeap of size 2, only stores negative cost
            negHeap = []
            if cost[node] > 0:
                posHeap.append(cost[node])
            else:
                # need a negative sign because negHeap is a max heap
                negHeap.append(-cost[node])

            # the size of the current subtree
            size = 1

            # collect and merge all extremas from subtrees
            for neighbor in graph[node]:
                if neighbor == parent:
                    # skip the parent node
                    continue
                subSize, subPosHeap, subNegHeap = dfs(neighbor, node)
                size += subSize
                # pos, min heap
                for c in subPosHeap:
                    heapq.heappush(posHeap, c)
                    if len(posHeap) > 3:
                        heapq.heappop(posHeap)
                # neg, max heap
                for c in subNegHeap:
                    heapq.heappush(negHeap, c)
                    if len(negHeap) > 2:
                        heapq.heappop(negHeap)

            if size < 3:
                coin[node] = 1
            else:
                # the lower bound of coin[node] is 0, so we always take a maximum
                if len(posHeap) == 3:
                    coin[node] = max(coin[node], posHeap[0] * posHeap[1] * posHeap[2])
                if len(negHeap) == 2 and posHeap:
                    coin[node] = max(coin[node], negHeap[0] * negHeap[1] * max(posHeap))

            return size, posHeap, negHeap
        
        # start from the root, the root does not have a parent
        dfs(0, -1)
        return coin
