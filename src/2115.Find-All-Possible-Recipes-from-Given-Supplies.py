from collections import defaultdict, deque

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        in_degrees = defaultdict(int)
        graph = defaultdict(list)
        q = deque()
        
        for supply in supplies:
            # Those are nodes with in_degree = 0
            q.append(supply)
            
        for i in range(len(recipes)):
            recipe = recipes[i]
            for ingredient in ingredients[i]:
                # Add an edge to the graph
                graph[ingredient].append(recipe)
                in_degrees[recipe] += 1
        
        res = []
        recipes_hs = set(recipes)
        # Run BFS topological sort
        while q:
            cur_node = q.popleft()
            if cur_node in recipes_hs:
                res.append(cur_node)
            for next_node in graph[cur_node]:
                in_degrees[next_node] -= 1
                if in_degrees[next_node] == 0:
                    q.append(next_node)
        
        return res