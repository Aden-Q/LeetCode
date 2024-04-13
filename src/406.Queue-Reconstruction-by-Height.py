class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # sorting first on height, decending
        # then on key, ascending
        people.sort(key = lambda x: (-x[0], x[1]))
        q = []
        for p in people:
            q.insert(p[1], p)
            
        return q