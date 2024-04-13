class Solution:
    def equalFrequency(self, word: str) -> bool:
        freq_counter = Counter(Counter(word).values())
        if len(freq_counter) == 1 and (1 in freq_counter or 1 in freq_counter.values()):
            return True

        if len(freq_counter) != 2:
            return False

        if freq_counter[1] == 1:
            return True
        
        sorted_freq = sorted(freq_counter.keys())
        if freq_counter[sorted_freq[1]] == 1 and sorted_freq[1] == sorted_freq[0] + 1:
            return True
        
        return False
