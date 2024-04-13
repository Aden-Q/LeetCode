class Solution:
    def search_in_range(self, nums, start, end, target):
        if end < start:
            return -1
        idx = (start + end) // 2
        if nums[idx] == target:
            return idx
        elif nums[idx] < nums[end]:
            if target > nums[idx] and target <= nums[end]:
                return self.search_in_range(nums, idx+1, end, target)
            else:
                return self.search_in_range(nums, start, idx-1, target)   
        else:
            if target < nums[idx] and target >= nums[start]:
                return self.search_in_range(nums, start, idx-1, target)
            else:
                return self.search_in_range(nums, idx+1, end, target)   
    
    def search(self, nums: List[int], target: int) -> int:
        return self.search_in_range(nums, 0, len(nums)-1, target)
        