class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x : x[0] - x[1])
        total_cost = 0
        
        for i in range(len(costs) // 2):
            total_cost += costs[i][0] + costs[i + len(costs) // 2][1]
            
        return total_cost