class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        ans = 0
        counter = Counter(words)
        mid = False

        for key in counter:
            if key[0] == key[1]:
                if counter[key] % 2 == 0:
                    ans += counter[key] * 2
                else:
                    ans += (counter[key] - 1) * 2
                    mid = True
            else:
                reverse = key[::-1]
                if counter[reverse] > 0:
                    num_pairs = min(counter[key], counter[reverse])
                    ans += num_pairs * 4
                    counter[key] -= num_pairs
                    counter[reverse] -= num_pairs

        return ans + 2 if mid else ans
