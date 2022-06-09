class Solution:
    def minSwaps(self, data: List[int]) -> int:
        num_ones = sum(data)
        if num_ones == 0:
            return 0
        left = 0
        right = num_ones - 1
        cur_cnt = sum(data[left:(right+1)])
        max_cnt = cur_cnt
        while right < len(data):
            if data[left] == 1:
                cur_cnt -= 1
            left += 1
            right += 1
            if right < len(data) and data[right] == 1:
                cur_cnt += 1
            max_cnt = max(max_cnt, cur_cnt)
            
        return num_ones - max_cnt