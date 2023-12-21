class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]

    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        # taking indices into s as nodes, we can build a DSU, finally we use divide and conquer
        # to construct a final sring
        # build a map: from UF root -> charset, each charset is sorted ascendingly
        # finally we iterate through s, for each index, pick the smllest character in the corresponding charset of the uf group
        n = len(s)
        uf = UnionFind(n)

        # union
        for pair in pairs:
            first, second = pair
            uf.union(first, second)

        charset_dict = defaultdict(list)
        for i in range(n):
            charset_dict[uf.find(i)].append(s[i])
        
        for key in charset_dict:
            heapq.heapify(charset_dict[key])

        # finally we can build the string
        res = ""
        for i in range(n):
            res += heapq.heappop(charset_dict[uf.find(i)])
        
        return res
