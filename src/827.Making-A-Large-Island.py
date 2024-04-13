class UF:
    def __init__(self, size):
        # -1 means this island does not exist, positive number means the island exist and the number is its root
        self.parent = [-1] * size
        # the size of this island, we only care about the rank of the root
        self.rank = [0] * size

    def add(self, x):
        self.parent[x] = x
        self.rank[x] = 1

        return
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            # already connected
            return
        
        # root_x is the new root
        self.parent[root_y] = root_x
        self.rank[root_x] += self.rank[root_y]

        return

    def getRank(self, x):
        return self.rank[self.find(x)]

    def getMaxRank(self):
        return max(self.rank)


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        # the first thing is to represent those islands as connected components with some size
        n = len(grid)
        zeros = set()
        uf = UF(n * n)

        for row in range(n):
            for col in range(n):
                idx = row * n + col
                if grid[row][col] == 0:
                    zeros.add((row, col))
                else:
                    # add it as an island
                    uf.add(idx)
                    # connect it to its neighbors
                    for prev_row, prev_col in [(row-1, col), (row, col-1)]:
                        if 0 <= prev_row < n and 0 <= prev_col < n and grid[prev_row][prev_col] == 1:
                            prev_idx = prev_row * n + prev_col
                            uf.union(prev_idx, idx)
        
        # now we have all islands, we need to iterate through all 0's to make a larger island
        max_rank = uf.getMaxRank()
        for row, col in zeros:
            # find all neigbor islands of this zero grid and connect them together
            rank = 1
            islands = set()
            for d in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                next_row, next_col = row + d[0], col + d[1]
                if 0 <= next_row < n and 0 <= next_col < n and grid[next_row][next_col] == 1:
                    idx = next_row * n + next_col
                    root = uf.find(idx)
                    # if two islands are connected before, we don't want to count them twice
                    if root not in islands:
                        islands.add(root)
                        rank += uf.getRank(root)
            
            max_rank = max(max_rank, rank)

        return max_rank
