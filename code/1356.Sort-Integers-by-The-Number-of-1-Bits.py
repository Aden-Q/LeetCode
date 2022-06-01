class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def count1s(num) -> int:
            cnt = 0
            while num != 0:
                cnt += num & 0x1
                num = num >> 1
            return cnt
        arr_next = [(num, count1s(num)) for num in arr]
        arr_next.sort(key = lambda a: (a[1], a[0]))
        return [item[0] for item in arr_next]