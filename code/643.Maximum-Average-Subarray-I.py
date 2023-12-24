class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left, right = 0, k - 1
        curr_sum = sum(nums[left:right+1])
        max_sum = curr_sum

        right +=1
        while right < len(nums):
            curr_sum += nums[right]
            curr_sum -= nums[left]
            max_sum = max(max_sum, curr_sum)
            left += 1
            right += 1

        return max_sum / k