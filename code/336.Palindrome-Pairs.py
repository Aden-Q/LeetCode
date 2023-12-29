class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        # The current word we are exploring can possibly be either a prefix or a postfix of some palindrome
        # We can safely assume the current word >= n / 2 if n is the length of the palindrome
        # Since otherwise, its counterpart will be the word we want to search for
        def getValidSuffixes(word):
            # we should consider empty string as a valid suffix string
            # we should consider the full string as a valid suffix string
            idx = len(word)
            ans = set()

            while idx >= 0:
                # if word[:idx] is a palindrome, then word[idx:] is a valid suffix string
                # we consider empty string as valid suffix string as well
                if word[:idx] == word[:idx][::-1]:
                    ans.add(word[idx:])
                idx -= 1

            return ans

        def getValidPrefixes(word):
            # we should consider empty string as a valid prefix string
            # we should consider the full string as a valid prefix string
            idx = 0
            ans = set()

            while idx < len(word):
                # if word[:idx] is a palindrome, then word[idx:] is a valid postfix string
                # we consider empty string as valid postfix string as well
                if word[idx:] ==  word[idx:][::-1]:
                    ans.add(word[:idx])
                idx += 1

            return ans

        word_table = {word: idx for idx, word in enumerate(words)}
        ans = []
        for idx, word in enumerate(words):
            for w in getValidSuffixes(word):
                reversed_w = w[::-1]
                # for each valid suffix, we try to find a prefix in the table
                if reversed_w in word_table and word_table[reversed_w] != idx:
                    ans.append([word_table[reversed_w], idx])
        
            for w in getValidPrefixes(word):
                reversed_w = w[::-1]
                # for each valid prefix, we try to find a suffix in the table
                if reversed_w in word_table and word_table[reversed_w] != idx:
                    ans.append([idx, word_table[reversed_w]])

        return ans
