class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        last_idx = -1
        for i in range(len(number)-1):
            if number[i] == digit:
                last_idx = i
                if number[i] < number[i+1]:
                    return number[:i] + number[i+1:]
        if number[-1] == digit:
            last_idx = len(number) - 1
        return number[:last_idx] + number[last_idx+1:]