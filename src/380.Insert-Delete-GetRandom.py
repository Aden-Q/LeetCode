import random

class RandomizedSet:
    def __init__(self):
        self.size = 0
        self.dict = {}
        self.arr = []
        
    def insert(self, val: int) -> bool:
        if val in self.dict.keys():
            return False
        self.arr.append(val)
        self.dict[val] = self.size
        self.size += 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dict.keys():
            return False
        idx = self.dict[val]
        self.dict[self.arr[-1]] = idx
        self.arr[idx], self.arr[-1] = self.arr[-1], self.arr[idx]
        self.arr.pop()
        del self.dict[val]
        self.size -= 1
        return True

    def getRandom(self) -> int:
        return self.arr[random.randint(0, self.size-1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()