class RandomizedSet:
    # What if we have duplicate values???
    def __init__(self):
        # The list used to store the element
        self.list = []
        # The size of the current list/dict, considering size == capacity
        self.size = 0
        # The dictionary maintains a mapping between a value and its index in to the list
        self.dict = {}
        
    def insert(self, val: int) -> bool:
        if val in self.dict:
            # The element already exists
            return False
        
        self.list.append(val)
        self.dict[val] = self.size
        self.size += 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False
        
        last_element, idx = self.list[-1], self.dict[val]
        self.list[idx], self.dict[last_element] = last_element, idx
        self.list.pop()
        self.size -= 1
        del self.dict[val]
        return True
        
    def getRandom(self) -> int:
        return random.choice(self.list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()