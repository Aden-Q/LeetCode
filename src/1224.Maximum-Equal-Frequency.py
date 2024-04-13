class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        # greedy, looking backward
        # count the frequency of all numbers
        counter = Counter(nums)
        # count the frequency of frequency
        freq_counter = Counter(counter.values())

        def feasible() -> bool:
            nonlocal freq_counter
            # if we only have 1 frequency and this frequency counter is 1, then all numbers are the same
            if len(freq_counter) == 1:
                for val in freq_counter.values():
                    if val == 1:
                        return True
                    elif freq_counter[1] > 0:
                        return True
            elif len(freq_counter) == 2:
                # then we only need a (key, value) pair to be (1, 1) to claim that it is feasible
                if freq_counter[1] == 1:
                    return True
                else:
                    keys = list(freq_counter.keys())
                    keys.sort()
                    if keys[1] == keys[0] + 1 and freq_counter[keys[1]] == 1:
                        return True

            return False

        # start with the full list
        if feasible():
            return len(nums)

        for num in nums[::-1]:
            # remove num from the prefix
            counter[num] -= 1
            new_freq = counter[num]
            if new_freq > 0:
                freq_counter[new_freq] += 1
            freq_counter[new_freq + 1] -= 1
            if freq_counter[new_freq + 1] == 0:
                del freq_counter[new_freq + 1]
            
            # check whether the current prefix is feasible
            if feasible():
                return sum(counter.values())
