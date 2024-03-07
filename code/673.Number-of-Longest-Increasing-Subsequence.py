class Solution:
    def maximumSwap(self, num: int) -> int:
        # store the rightmost index of each integer
        # -1 if not exists
        last_index = [-1] * 10
        digits = list(str(num))

        for idx in range(len(digits)):
            last_index[int(digits[idx])] = idx

        for idx in range(len(digits)):
            for k in range(9, int(digits[idx]), -1):
                # find if there exists a number greater than the curent digit to its right side
                if last_index[k] > idx:
                    # swap and return
                    digits[last_index[k]], digits[idx] = digits[idx], digits[last_index[k]]
                    return int(''.join(digits))

        return num
