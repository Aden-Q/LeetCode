import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(nums, low, high):
            pivot = nums[low]
            i = low + 1
            j = high
            while i <= j:
                while i < high and nums[i] <= pivot:
                    i += 1
                while j > low and nums[j] > pivot:
                    j -= 1
                if i >= j:
                    break
                nums[i], nums[j] = nums[j], nums[i]
                
            nums[low], nums[j] = nums[j], nums[low]
            return j
        
        random.shuffle(nums)
        low = 0
        high = len(nums) - 1
        k = len(nums) - k
        while low <= high:
            p = partition(nums, low, high)
            if p < k:
                low = p + 1
            elif p > k:
                high = p - 1
            else:
                return nums[p]
        return -1