class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # count the number of subarrays have t odd numbers in it
        freq_counter = Counter()
        freq_counter[0] = 1
        num_odd_numbers = 0
        ans = 0
        for num in nums:
            if num % 2 == 1:
                num_odd_numbers += 1
            
            ans += freq_counter[num_odd_numbers - k]
            freq_counter[num_odd_numbers] += 1

        return ans
