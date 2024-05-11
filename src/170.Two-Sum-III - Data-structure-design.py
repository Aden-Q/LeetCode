class TwoSum:

    def __init__(self):
        self.counter = Counter()
        

    def add(self, number: int) -> None:
        self.counter[number] += 1

    def find(self, value: int) -> bool:
        for key in self.counter:
            if value - key != key and self.counter[value-key] > 0:
                return True
            if value - key == key and self.counter[key] > 1:
                return True

        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)