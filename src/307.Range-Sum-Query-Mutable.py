class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        # 1-indexed segment tree
        self.tree = [0] * (4 * self.n + 1)
        self._build(nums, 1, 0, self.n-1)
        
    def _build(self, arr, treeIdx, lo, hi) -> None:
        if lo == hi:
            self.tree[treeIdx] = arr[lo]
            return
        
        mid = (lo + hi) // 2
        self._build(arr, 2 * treeIdx, lo, mid)
        self._build(arr, 2 * treeIdx + 1, mid+1, hi)

        self.tree[treeIdx] = self._merge(2 * treeIdx, 2 * treeIdx + 1)

    def _merge(self, treeIdx1, treeIdx2) -> int:
        return self.tree[treeIdx1] + self.tree[treeIdx2]

    def _update(self, treeIdx, lo, hi, arrIdx, val) -> None:
        if lo == hi:
            self.tree[treeIdx] = val
            return

        mid = (lo + hi) // 2
        if arrIdx > mid:
            self._update(2 * treeIdx + 1, mid+1, hi, arrIdx, val)
        else:
            self._update(2 * treeIdx, lo, mid, arrIdx, val)

        self.tree[treeIdx] = self._merge(2 * treeIdx, 2 * treeIdx + 1)
    
    def _query(self, treeIdx, lo, hi, left, right) -> int:
        if left > hi or right < lo:
            return 0

        if left <= lo and right >= hi:
            return self.tree[treeIdx]

        mid = (lo + hi) // 2
        return self._query(2 * treeIdx, lo, mid, left, min(right, mid)) + self._query(2 * treeIdx + 1, mid+1, hi, max(mid+1, left), right)

    def update(self, index: int, val: int) -> None:
        self._update(1, 0, self.n-1, index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self._query(1, 0, self.n-1, left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)