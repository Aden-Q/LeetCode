class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        similar_dt = defaultdict(set)
        for pair in similarPairs:
            similar_dt[pair[0]].add(pair[1])
            similar_dt[pair[1]].add(pair[0])
        
        for idx in range(len(sentence1)):
            if sentence1[idx] == sentence2[idx]:
                continue
            if sentence2[idx] not in similar_dt[sentence1[idx]]:
                return False

        return True
