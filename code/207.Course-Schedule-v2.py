class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degrees = [0] * numCourses
        # directed graph
        graph = [[] for _ in range(numCourses)]
        initial_courses = set(range(numCourses))
        
        for edge in prerequisites:
            first, second = edge
            in_degrees[second] += 1
            graph[first].append(second)
            if second in initial_courses:
                initial_courses.remove(second)
                
        cnt = 0
        while initial_courses:
            cur = initial_courses.pop()
            cnt += 1
            for next_course in graph[cur]:
                in_degrees[next_course] -= 1
                if in_degrees[next_course] == 0:
                    initial_courses.add(next_course)
        
        return cnt == numCourses