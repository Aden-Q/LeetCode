class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # It's a O(|V| + |E|) time and O(|V| + |E|) space solution
        # using the adjacency list
        in_degrees = [0] * numCourses
        graph = [[] for _ in range(numCourses)]
        
        q = set(range(numCourses))
        
        for first, second in prerequisites:
            graph[second].append(first)
            in_degrees[first] += 1
            if first in q:
                q.remove(first)
        
        res = []
        while q:
            cur = q.pop()
            res.append(cur)
            for next_course in graph[cur]:
                in_degrees[next_course] -= 1
                if in_degrees[next_course] == 0:
                    q.add(next_course)
        
        if len(res) == numCourses:
            return res
        return []