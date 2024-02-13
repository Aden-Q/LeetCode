class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for row in range(len(words)):
            word = words[row]
            for col in range(len(word)):
                if col >= len(words) or row >= len(words[col]) or words[col][row] != words[row][col]:
                    return False
        
        return True
