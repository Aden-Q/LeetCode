class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        # a map between abbreviation and a set of words of this abbreviation
        self.t = defaultdict(set)
        
        for word in dictionary:
            abbrev = self.getAbbrev(word)
            self.t[abbrev].add(word)

    def getAbbrev(self, word: str) -> str:
        if len(word) < 3:
            return word
        
        return word[0] + str(len(word) - 2) + word[-1]

    def isUnique(self, word: str) -> bool:
        abbrev = self.getAbbrev(word)
        if abbrev not in self.t or (len(self.t[abbrev]) == 1 and word in self.t[abbrev]):
            return True

        return False


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)