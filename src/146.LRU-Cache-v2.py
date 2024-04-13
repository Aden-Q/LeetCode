# A very typical implementation of LRU cache is a (doubly) linked list + hash table
class ListNode:
    def __init__(self, key = 0, val = 0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = ListNode(key = -1)  # A dummy head, must use an invalid key
        self.tail = ListNode(key = -1)  # A dummy tail, must use an invalid key
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        # A map between a key to a list node for quick find
        self.mp = {}

    def get(self, key: int) -> int:
        # A quick question to ask is when we visit a node, whether we should
        # push it to the front of the linked list (i.e. the most frequently used one)
        # Normally we should do this
        if key not in self.mp:
            return -1
        # Otherwise the key exists, we need to move it to the head
        # First delete
        curr_node = self.mp[key]
        curr_node.prev.next = curr_node.next
        curr_node.next.prev = curr_node.prev
        # Then insert to the head
        # dummy_head -> real head
        curr_node.prev = self.head
        curr_node.next = self.head.next
        self.head.next.prev = curr_node
        self.head.next = curr_node
        return self.mp[key].val
        

    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            # The key exists, we need to move this node to the front of the linked list
            # prev_node -> curr_node -> next_node
            # First delete
            curr_node = self.mp[key]
            curr_node.prev.next = curr_node.next
            curr_node.next.prev = curr_node.prev
            curr_node.val = value
        else:
            curr_node = ListNode(key = key, val = value)
            self.mp[key] = curr_node
        # Then insert to the head
        # dummy_head -> real head
        curr_node.prev = self.head
        curr_node.next = self.head.next
        self.head.next.prev = curr_node
        self.head.next = curr_node
        # If exceed the capacity, delete the last ndoe
        if len(self.mp.keys()) > self.capacity:
            # Delte the tail
            # prev -> real tail -> dummy tail
            key_to_delete = self.tail.prev.key
            self.tail.prev.prev.next = self.tail
            self.tail.prev = self.tail.prev.prev
            del self.mp[key_to_delete]
            
        
        
            
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)