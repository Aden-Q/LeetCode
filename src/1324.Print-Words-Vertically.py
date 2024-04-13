class Solution:
    def printVertically(self, s: str) -> List[str]:
        res = []
        s = s.split()

        num_words = max([len(w) for w in s])

        for col_idx in range(num_words):
            curr_word = [w[col_idx] if col_idx < len(w) else ' ' for w in s]
            curr_word = ''.join(curr_word).rstrip()
            res.append(curr_word)

        return res
