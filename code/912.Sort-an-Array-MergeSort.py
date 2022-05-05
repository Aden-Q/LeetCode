class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(nums, low, high):
            if low >= high:
                return
            mid = (low + high) // 2
            mergeSort(nums, low, mid)
            mergeSort(nums, mid+1, high)
            merge(nums, low, mid, high)
            return
            
        def merge(nums, low, mid, high):
            res = []
            idx1 = low
            idx2 = mid + 1
            while idx1 <= mid and idx2 <= high:
                if nums[idx1] <= nums[idx2]:
                    res.append(nums[idx1])
                    idx1 += 1
                else:
                    res.append(nums[idx2])
                    idx2 += 1
            while idx1 <= mid:
                res.append(nums[idx1])
                idx1 += 1
            while idx2 <= mid:
                res.append(nums[idx2])
                idx2 += 1
            # copy back
            for i in range(len(res)):
                nums[low + i] = res[i]
                
            return
                 
        mergeSort(nums, 0, len(nums) - 1)
        return nums    