class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        # we can sort the input array
        # then in a greedy manner, we partition the input array from start to the end
        nums.sort()
        start = 0
        cnt = 0

        # for each start index, we search for the end
        # each partitioned array should be [start, end), including the start and excluding the end
        while start < len(nums):
            end = bisect.bisect_right(nums, nums[start] + k, lo=start)
            cnt += 1
            start = end

        return cnt