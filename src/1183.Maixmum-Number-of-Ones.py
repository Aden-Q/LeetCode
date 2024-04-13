class Solution:
    def maximumNumberOfOnes(self, width: int, height: int, sideLength: int, maxOnes: int) -> int:
        if sideLength * sideLength <= maxOnes:
            # this is a extreme case
            return width * height

        max_heap = []
        for row in range(sideLength):
            for col in range(sideLength):
                val = ((height - col - 1) // sideLength + 1) * ((width - row - 1) // sideLength + 1)
                heapq.heappush(max_heap, -val)

        res = 0
        while maxOnes:
            maxOnes -= 1
            curr_val = heapq.heappop(max_heap)
            res += -curr_val

        return res
