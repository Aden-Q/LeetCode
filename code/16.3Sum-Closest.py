class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        bestSum = nums[0] + nums[1] + nums[2]
        bestAbs = math.inf

        for pivot in range(len(nums) - 2):
            # run 2 sums using elements to the right of nums[pivot]
            left, right = pivot + 1, len(nums) - 1
            while left < right:
                currSum = nums[pivot] + nums[left] + nums[right]
                currAbs = abs(currSum - target)
                if currAbs < bestAbs:
                    bestAbs = currAbs
                    bestSum = currSum

                if currSum == target:
                    return target
                elif currSum > target:
                    right -= 1
                else:
                    left += 1

        return bestSum
