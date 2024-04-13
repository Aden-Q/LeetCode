class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)
        min_heap = []
        curr_max = -float('inf')

        for i in range(k):
            head = nums[i][0]
            curr_max = max(curr_max, head)
            # each heap element is a tuple: (value, list index, num index in the list)
            heapq.heappush(min_heap, (head, i, 0))

        optimal_range = [min_heap[0][0], curr_max]
        # we keep updating the optimal range if we ever find a smaller range
        while True:
            val, list_idx, idx = heapq.heappop(min_heap)
            if idx == len(nums[list_idx]) - 1:
                # this is the last element in that list, we cannot do further work
                break
            # otherwise we update the curr_range and the min_heap
            # push the next element into the heap
            heappush(min_heap, (nums[list_idx][idx+1], list_idx, idx+1))
            curr_max = max(curr_max, nums[list_idx][idx+1])
            curr_min = min_heap[0][0]
            if curr_max - curr_min < optimal_range[1] - optimal_range[0]:
                optimal_range = [curr_min, curr_max]
            elif curr_max - curr_min == optimal_range[1] - optimal_range[0] and curr_min < optimal_range[0]:
                optimal_range = [curr_min, curr_max]
        
        return optimal_range
