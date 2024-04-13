# we use a doubly linkedlist for quick insertion
class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        # sentinel nodes for the doubly linkedlist
        # from head to tail, the least frequently used to the most frequently used
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        # a map from a key to a Node in the linkedlist, in order to quickly find the node for insertion and deletion
        self.dic = defaultdict(Node)

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        # for a successfuly lookup, we need to do 2 things
        # 1. move the node to the tail of the linkedlist
        # 2. return the value associated with the key
        node = self.dic[key]
        self.remove_node(node)
        self.insert_node(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            node = self.dic[key]
            node.val = value
            self.remove_node(node)
            self.insert_node(node)
        else:
            # the node does not exist, we simply insert a new node into the tail
            node = Node(key=key, val=value)
            # insert the node before the tail
            self.insert_node(node)
            # insert into the dic
            self.dic[key] = node

            # check if it's oversized
            if len(self.dic) > self.capacity:
                node_to_delete = self.head.next
                self.remove_node(self.head.next)
                del self.dic[node_to_delete.key]
        
        return

    def insert_node(self, node) -> None:
        # insert the node before the tail
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node

        return

    def remove_node(self, node) -> None:
        # remove the node from the original position
        node.prev.next = node.next
        node.next.prev = node.prev

        return

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)