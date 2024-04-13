class UF:
    def __init__(self, size):
        self.size = size
        self.parent = [i for i in range(size)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        self.parent[root_x] = root_y

        return

    def connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        answer = [False] * len(queries)
        uf = UF(n + 1)

        for city in range(max(threshold+1, 1), n+1):
            for next_city in range(city*2, n+1, city):
                uf.union(city, next_city)

        for i in range(len(queries)):
            x, y = queries[i]
            if uf.connected(x, y):
                answer[i] = True

        return answer
