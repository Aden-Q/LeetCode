class SnapshotArray:

    def __init__(self, length: int):
        # a global snapshot id
        self.id = 0
        self.history = [[[0, 0]] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        if self.history[index][-1][0] < self.id:
            # we need a new snapshot
            self.history[index].append([self.id, val])
        else:
            # otherwise we just need to update the latest snapshot
            self.history[index][-1][1] = val

    def snap(self) -> int:
        self.id += 1
        return self.id - 1

    def get(self, index: int, snap_id: int) -> int:
        snapshot = self.history[index]
        left, right = 0, len(snapshot)
        while left < right:
            mid = left + (right - left) // 2
            if snapshot[mid][0] == snap_id:
                return snapshot[mid][1]
            elif snapshot[mid][0] < snap_id:
                left = mid + 1
            else:
                right = mid
        
        return snapshot[right-1][1]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)