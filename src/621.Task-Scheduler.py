class Node:
    def __init__(self, task=None, num=None):
        self.task = task
        self.num = num

    # to make it a max heap based on the frequency of tasks
    def __lt__(self, other):
        return self.num > other.num

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Let M be the number of distinct tasks
        # Let L be the total number of tasks
        # O(L)
        counter = Counter(tasks)
        heap = [Node(task, num) for task, num in counter.items()]
        # O(M)
        heapq.heapify(heap)
        for node in heap:
            print(node.task, node.num)

        steps = 0
        while heap:
            remain = []
            idle = 0
            for _ in range(n + 1):
                if heap:
                    node = heapq.heappop(heap)
                    steps += 1
                    if node.num > 1:
                        node.num -= 1
                        remain.append(node)
                else:
                    idle += 1
                
            for node in remain:
                heapq.heappush(heap, node)
                
            if not heap:
                break
                
            steps += idle

        return steps