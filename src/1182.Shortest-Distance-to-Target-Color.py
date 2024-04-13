class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        # Preprocessing: use a hashmap to store
        # the indices of each color occuring in the colors array
        hash_map = {1: [], 2: [], 3: []}
        for idx, val in enumerate(colors):
            hash_map[val].append(idx)
        # Sort the hash_map, O(n log n)
        for key in [1, 2, 3]:
            hash_map[key].sort()
        
        res = []
        for i, c in queries:
            if len(hash_map[c]) == 0:
                # no such a color in the colors array
                res.append(-1)
            else:
                # do a binary search to find the nearest index to that color
                idx = bisect.bisect_left(hash_map[c], i)
                left = abs(hash_map[c][max(idx-1, 0)] - i)
                right = abs(hash_map[c][min(idx, len(hash_map[c]) - 1)] - i)
                res.append(min(left, right))
        return res