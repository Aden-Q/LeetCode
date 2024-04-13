class UnionFind():
    def __init__(self, size, wells):
        self.parent = [i for i in range(size+1)]
        # well cost for each group
        # note that for a connecteed component, the well cost for the group is recorded in its root node
        # i.e. self.well_cost[root], this can reduce time complexity when we need to update the array
        self.well_cost = [0] + wells

    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        # new root will be the group with lower well cost
        if self.well_cost[root_x] < self.well_cost[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_x] = root_y

    def connected(self, x, y):
        return self.find(x) == self.find(y)

    def getGroupWellCost(self, x):
        return self.well_cost[self.find(x)]

class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        # greedy
        # we start with building a well or each house, whose cost is maximum initially
        # then we iterateover pipes to find paths to connect houses to reduce cost
        # we need to sort the pipe based on the building cost ascendingly
        # and for each pipe, determine if it's worth to build comparing to the cost of building wells individually for each group
        # initial cost
        uf = UnionFind(n, wells)
        pipes.sort(key = lambda x: x[2])
        total_pipe_cost = 0
        total_well_cost = 0

        for pipe in pipes:
            house1, house2, pipe_cost = pipe
            # if they are already connected, we don't need to build an additional pipe
            if uf.connected(house1, house2):
                continue
            # we need to determine if it's worthy to union two groups
            # the net gain of unioning 2 groups is the reduction of a single well cost - pipe cost
            # if this number if positive, then we union. Otherwise we don't
            well_cost_group1, well_cost_group2 = uf.getGroupWellCost(uf.find(house1)), uf.getGroupWellCost(uf.find(house2))
            if max(well_cost_group1, well_cost_group2) - pipe_cost > 0:
                uf.union(house1, house2)
                total_pipe_cost += pipe_cost

        # add well cost for each group
        group_ids = set()
        for i in range(1, n+1):
            group_ids.add(uf.find(i))
        
        for group in group_ids:
            total_well_cost += uf.getGroupWellCost(group)
        
        return total_pipe_cost + total_well_cost
