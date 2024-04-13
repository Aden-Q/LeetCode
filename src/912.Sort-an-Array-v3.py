import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # shuffle the array
        random.shuffle(nums)
        def quickSort(nums, low, high):
            if low >= high:
                return
            p = partition(nums, low, high)
            quickSort(nums, low, p-1)
            quickSort(nums, p+1, high)
            return
        
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
            
        quickSort(nums, 0, len(nums) - 1)
        return nums  