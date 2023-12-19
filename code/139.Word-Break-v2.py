class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict_hs = set(wordDict)
        word_len_iterator = [len(word) for word in wordDict]
        min_word_len = min(word_len_iterator)
        max_word_len = max(word_len_iterator)

        # because the same word can be used multiple times,
        # there are potential overlapping sub problems so use a memo table to optimize
        @lru_cache(None)
        def dfs(s) -> bool:
            if len(s) == 0:
                return True
            # check a prefix whose length is within min_word_len ~ max_word_len
            # is more efficient given the conditions
            # O(max_word_len)
            for prefix_len in range(min_word_len, max_word_len + 1):
                prefix = s[:prefix_len]
                if prefix in wordDict_hs and dfs(s[prefix_len:]):
                    return True

            return False

        return dfs(s)