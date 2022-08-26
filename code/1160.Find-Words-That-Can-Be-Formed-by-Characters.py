from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_counter = Counter(chars)
        res = 0
        
        for word in words:
            word_counter = Counter(word)
            is_good = True
            for key, val in word_counter.items():
                if val > chars_counter[key]:
                    # Not a good word
                    is_good = False
                    break
            if is_good:
                res += len(word)
                
        return res