class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        from sortedcontainers import SortedList
        all_freq = SortedList([0] * len(set(nums)))
        
        counter = Counter()
        for i in range(n):
            prev_freq = counter[nums[i]]
            curr_freq = prev_freq + freq[i]
            counter[nums[i]] = curr_freq
            all_freq.remove(prev_freq)
            all_freq.add(curr_freq)
            ans[i] = all_freq[-1]
            
        return ans
