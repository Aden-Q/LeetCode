class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        # O(n)
        # subarrayWithAtMost returns the number of subarrays with at most t different integers
        def subarrayWithAtMost(t) -> int:
            # sliding window
            ans = 0
            # the counter is the current window
            counter = Counter()
            left, right = 0, 0
            while right < len(nums):
                counter[nums[right]] += 1
                while len(counter) > t:
                    # contract the window
                    counter[nums[left]] -= 1
                    if counter[nums[left]] == 0:
                        del counter[nums[left]]
                    left += 1

                # (right - left + 1) subarrays ending at nums[right] satisfy the condition
                ans += right - left + 1
                right += 1

            return ans

        return subarrayWithAtMost(k) - subarrayWithAtMost(k-1)
