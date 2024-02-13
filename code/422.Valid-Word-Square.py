class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for row in range(len(words)):
            for col in range(len(words[row])):
                if col >= len(words) or row >= len(words[col]) or words[col][row] != words[row][col]:
                    return False
        
        return True
