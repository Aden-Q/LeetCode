class TimeMap:

    def __init__(self):
        # key-value pairs are stored in a dict
        # value takes the form: (timestamp, value)
        self.dict = defaultdict(list)
    
    # O(1)
    def set(self, key: str, value: str, timestamp: int) -> None:
        # given the fact that timestamp is strictly increasing, we append new value pairs to the end of the list
        self.dict[key].append((timestamp, value))

    # O(log n)
    def get(self, key: str, timestamp: int) -> str:
        t = self.dict[key]
        if len(t) == 0:
            return ""

        # find the right most element that is less than or equal to the given timestamp
        left, right = 0, len(t) - 1
        while left <= right:
            mid = (right - left) // 2 + left
            if t[mid][0] == timestamp:
                # found a matching timestamp, return the associated value immediately
                return t[mid][1]
            elif t[mid][0] < timestamp:
                left = mid + 1
            else:
                right = mid - 1
        # left - 1 is the target index
        if left - 1 >= 0:
            return t[left-1][1]
        
        return ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)