class Solution:
    def kthLuckyNumber(self, k: int) -> str:
        # we can encode 4 to be 0 and 7 to be 1
        # then finding the kth lucky number is equivalent to finding
        # the decoded string of k+1 in its binary repesentation, dropping the MSB
        ans = list(bin(k+1)[3:])
        for i in range(len(ans)):
            if ans[i] == '0':
                ans[i] = '4'
            else:
                ans[i] = '7'

        return ''.join(ans)
