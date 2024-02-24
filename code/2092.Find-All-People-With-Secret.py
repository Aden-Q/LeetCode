class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        graph = defaultdict(list)
        for x, y, t in meetings:
            graph[x].append((y, t))
            graph[y].append((x, t))

        earliest = [float('inf')] * n
        earliest[0] = 0
        earliest[firstPerson] = 0

        q = deque()
        q.append((0, 0))
        q.append((firstPerson, 0))

        while q:
            person, timestamp = q.popleft()
            for next_person, next_timestamp in graph[person]:
                if next_timestamp < timestamp or earliest[next_person] <= timestamp:
                    continue
                earliest[next_person] = next_timestamp
                q.append((next_person, next_timestamp))

        return [i for i in range(n) if earliest[i] != float('inf')]
