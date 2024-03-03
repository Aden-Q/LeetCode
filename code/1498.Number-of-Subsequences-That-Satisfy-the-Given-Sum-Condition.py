class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        # nlogn time
        nums.sort()
        mod = 10 ** 9 + 7
        cnt = 0
        n = len(nums)
        for i in range(n):
            # search for nums[j] such that j is the right most index such that nums[i] + nums[j] <= target
            left, right = i, n
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] + nums[i] > target:
                    right = mid
                else:
                    left = mid + 1
            # calculate the number of subsequence between nums[i] ... nums[j], excluding nums[j], must use nums[i]
            if right == i:
                continue
            cnt = (cnt + 2 ** (right - i - 1)) % mod

        return cnt
