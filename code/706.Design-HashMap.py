class MyHashMap:

    def __init__(self):
        self.hash_dict = [''] * (10 ** 6 + 1)

    def put(self, key: int, value: int) -> None:
        self.hash_dict[key] = value

    def get(self, key: int) -> int:
        if self.hash_dict[key] == '':
            return -1
        else:
            return self.hash_dict[key]

    def remove(self, key: int) -> None:
        self.hash_dict[key] = ''
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)