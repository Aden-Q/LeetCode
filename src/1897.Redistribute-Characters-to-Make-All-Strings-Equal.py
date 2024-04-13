class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        counter = Counter()
        for word in words:
            counter += Counter(word)

        # find the gcd of all frequencies, if it's > 1 and <= len(words), then yes
        d = len(words)
        # test if d can divide all frequencies in the set
        # if not, then false, otherwise true
        for f in counter.values():
            if f % d != 0:
                return False
        
        return True
