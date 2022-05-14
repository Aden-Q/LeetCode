class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num_str = str(num)
        count = 0
        for i in range(len(num_str) - k + 1):
            cur = int(num_str[i:i+k])
            if cur != 0 and num % cur == 0:
                count += 1
        return count