class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ch_idx = word.find(ch)
        if ch_idx < 0:
            return word

        return word[:ch_idx+1][::-1] + word[ch_idx+1:]
