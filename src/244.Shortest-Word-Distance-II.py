class WordDistance:
    def __init__(self, wordsDict: List[str]):
        # each word is store in a hash map, with word string as the key and all its indices as the value
        # grouped in a list
        self.table = defaultdict(list)
        for idx, word in enumerate(wordsDict):
            self.table[word].append(idx)
        
        # quick look aside buffer for the same queries
        self.cache = defaultdict(int)

    def shortest(self, word1: str, word2: str) -> int:
        if (word1, word2) in self.cache:
            return self.cache[(word1, word2)]

        idx_list1 = self.table[word1]
        idx_list2 = self.table[word2]

        ptr1, ptr2 = 0, 0
        min_dist = math.inf
        # linear in O(len(idx_list1) + len(idx_list2))
        while ptr1 < len(idx_list1) and ptr2 < len(idx_list2):
            min_dist = min(min_dist, abs(idx_list1[ptr1] - idx_list2[ptr2]))
            if idx_list1[ptr1] < idx_list2[ptr2]:
                ptr1 += 1
            else:
                ptr2 += 1

        self.cache[(word1, word2)] = min_dist
        return min_dist

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)