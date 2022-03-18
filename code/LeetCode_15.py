# 15. 3Sum Double pointer
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        arr_size = len(nums)
        res = []
        for index in range(arr_size-2):
            if index >= 1 and nums[index] == nums[index - 1]:
                continue
            # initial value for pointers
            left_ptr = index + 1
            right_ptr = arr_size-1
            num1 = nums[index]
            while left_ptr < right_ptr:
                num2 = nums[left_ptr]
                num3 = nums[right_ptr]
                sum_temp = num1 + num2 + num3
                if sum_temp < 0:
                    # move the left pointer to the right to increase the sum
                    left_ptr += 1
                elif sum_temp > 0:
                    # move the right pointer to the left to decrease the sum
                    right_ptr -= 1
                # remove duplicates
                else:
                    while right_ptr > left_ptr and nums[right_ptr] == nums[right_ptr-1]:
                        right_ptr -= 1
                    while right_ptr > left_ptr and nums[left_ptr] == nums[left_ptr+1]:
                        left_ptr += 1
                    res.append([num1, num2, num3])
                    # initialize a new round
                    left_ptr += 1
                    right_ptr -= 1

        return res