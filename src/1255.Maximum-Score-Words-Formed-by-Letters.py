class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def letterToScore(l: str) -> int:
            idx = ord(l) - ord('a')
            return score[idx]

        letters = Counter(letters)
        maxScore = 0

        def dfs(idx, score, unusedLetters):
            nonlocal maxScore
            if idx == len(words):
                maxScore = max(maxScore, score)
                return

            # 2 options: taking the current word, or not
            # not taking
            dfs(idx+1, score, unusedLetters)

            # take
            if Counter(words[idx]) < unusedLetters:
                for c in words[idx]:
                    unusedLetters[c] -= 1
                    score += letterToScore(c)

                dfs(idx+1, score, unusedLetters)

                # backtrack
                for c in words[idx]:
                    unusedLetters[c] += 1
            
            return

        dfs(0, 0, letters)
        return maxScore
