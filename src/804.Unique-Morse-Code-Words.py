class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        maps = [".-","-...","-.-.","-..",".","..-.","--.","....", "..",
                ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-"
                ,"...-",".--","-..-","-.--","--.."]
        res = set()
        for word in words:
            word_trans = "".join([maps[ord(c) - ord('a')] for c in word])
            res.add(word_trans)
        
        return len(res)