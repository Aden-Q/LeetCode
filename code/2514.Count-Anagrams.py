class Solution:
    def countAnagrams(self, s: str) -> int:
        mod = 10 ** 9 + 7
        
        # given a word (i.e. no space in it)
        # count the number of its permutation
        def countPermutation(word) -> int:
            counter = Counter(word)
            cnt = math.factorial(len(word))
            for val in counter.values():
                if val > 1:
                    cnt //= math.factorial(val)
            
            return cnt % mod

        ans = 1
        words = s.split()
        for word in words:
            ans = (ans * countPermutation(word)) % mod

        return ans
