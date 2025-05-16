class Solution:
    def getWordsInLongestSubsequence(
        self, words: List[str], groups: List[int]
    ) -> List[str]:
        # a helper function. Given 2 words words[idx1] and words[idx2], check whether:
        # 1. words[idx1] and words[idx2] are equal in length
        # 2. The hamming distance betwee them is 1
        # 3. groups[idx1] != groups[idx2]
        # return true if both are true, otherwise false
        def diff(idx1, idx2) -> bool:
            word1, word2 = words[idx1], words[idx2]
            if len(word1) != len(word2) or groups[idx1] == groups[idx2]:
                return False

            n = len(word1)
            dist = 0
            for i in range(n):
                if word1[i] != word2[i]:
                    dist += 1
                # early break
                if dist > 1:
                    return False

            return dist == 1

        n = len(words)
        # dp[i] is the length of the longest sequence ending with words[i]
        dp = [1] * n
        # track backward the index of the previous word in such a sequence
        prev = [-1] * n

        for i in range(1, n):
            for j in range(i):
                if diff(i, j) and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j
        index = dp.index(max(dp))
        ans = []

        while index != -1:
            ans.append(words[index])
            index = prev[index]

        return ans[::-1]
