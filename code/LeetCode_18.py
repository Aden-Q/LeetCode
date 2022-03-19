class Solution:
    def fourSum(self, nums, target):
        if len(nums) == 0:
            return []
        res = []
        nums.sort()
        a = 0
        d = len(nums) - 1
        while a <= len(nums) - 4:
            if d < a + 3:
                # revoke
                d = len(nums) - 1
                # get new a
                while a <= d -3 and nums[a] == nums[a+1]:
                    a += 1
                a += 1
                if a >  d - 3:
                    break
            b = a+1
            c = d-1
            num1 = nums[a]
            num4 = nums[d]
            while b < c:
                num2 = nums[b]
                num3 = nums[c]
                sum_temp = num1 + num2 + num3 + num4
                # print(sum_temp)
                if sum_temp < target:
                    # move the start poniter to the right
                    b += 1
                elif sum_temp > target:
                    c -= 1
                else:
                    res.append([num1,num2,num3,num4])
                    while b < c and nums[b] == nums[b+1]:
                        b += 1
                    while b < c and nums[c] == nums[c-1]:
                        c -= 1
                    b += 1
                    c -= 1
            while d >= a + 3 and nums[d] == nums[d-1]:
                d -= 1
            d -= 1
        return res