class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Vector2D:

    def __init__(self, vec: List[List[int]]):
        # a dummy header
        self.head = ListNode()
        self.curr = self.head
        for row in vec:
            # each row is a collection of ints
            for num in row:
                self.curr.next = ListNode(num)
                self.curr = self.curr.next
        self.curr = self.head.next

    def next(self) -> int:
        res = self.curr.val
        self.curr = self.curr.next
        return res
        
    def hasNext(self) -> bool:
        return self.curr != None
        


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()