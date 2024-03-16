class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr1, arr2 = [(nums[0], 0)], [(nums[1], 1)]
        for i in range(2, n):
            idx1, idx2 = bisect.bisect_right(arr1, nums[i], key=lambda x: x[0]), bisect.bisect_right(arr2, nums[i], key=lambda x: x[0])
            greaterCount1, greaterCount2 = len(arr1) - idx1, len(arr2) - idx2
            if greaterCount1 > greaterCount2:
                arr1.insert(idx1, (nums[i], i))
            elif greaterCount1 < greaterCount2:
                arr2.insert(idx2, (nums[i], i))
            elif len(arr2) < len(arr1):
                arr2.insert(idx2, (nums[i], i))
            else:
                arr1.insert(idx1, (nums[i], i))
                
        arr1.sort(key=lambda x: x[1])
        arr2.sort(key=lambda x: x[1])

        return [e[0] for e in arr1] + [e[0] for e in arr2]
