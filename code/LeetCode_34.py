class Solution:
    def binary_search_last(self, nums, start, end, target):
        if start > end:
            return -1
        mid = (start + end) // 2
        if nums[mid] == target:
            next_idx = self.binary_search_last(nums, mid + 1, end, target)
            if next_idx == -1:
                return mid
            else:
                return next_idx
        elif nums[mid] < target:
            return self.binary_search_last(nums, mid + 1, end, target)
        else:
            return self.binary_search_last(nums, start, mid-1, target)

    def binary_search_first(self, nums, start, end, target):
        if start > end:
            return -1
        mid = (start + end) // 2
        if nums[mid] == target:
            next_idx = self.binary_search_first(nums, start, mid-1, target)
            if next_idx == -1:
                return mid
            else:
                return next_idx
        elif nums[mid] < target:
            return self.binary_search_first(nums, mid + 1, end, target)
        else:
            return self.binary_search_first(nums, start, mid-1, target)
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 1:
            return [-1,-1]
        
        return [self.binary_search_first(nums, 0, len(nums)-1, target), self.binary_search_last(nums, 0, len(nums)-1, target)]
        