class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # a max heap to keep track of the cost
        pq = []



        idx = 0
        while idx < len(heights) - 1:
            if heights[idx+1] > heights[idx]:
                cost = heights[idx+1] - heights[idx]
                if cost <= bricks:
                    # yes we can jump to the next building using bricks
                    heapq.heappush(pq, -cost)
                    bricks -= cost
                elif ladders > 0:
                    # bricks left are not enough, so we need to use a ladder
                    ladders -= 1
                    heapq.heappush(pq, -cost)
                    bricks += -heapq.heappop(pq) - cost
                else:
                    break

            idx += 1

        return idx
