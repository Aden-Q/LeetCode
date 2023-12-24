class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first_num = 1 << 31
        second_num = 1 << 31
        for n in nums:
            if n <= first_num:
                first_num = n
            elif n <= second_num:
                second_num = n
            else:
                return True

        return False