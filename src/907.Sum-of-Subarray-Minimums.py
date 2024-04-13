class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # Monotonical stack
        nextSmaller = [len(arr)] * len(arr)
        prevSmaller = [-1] * len(arr)
        
        st = []
        for i in range(len(arr)):
            while st and arr[st[-1]] >= arr[i]:
                nextSmaller[st.pop()] = i
            st.append(i)
        
        st = []
        for i in range(len(arr)-1, -1, -1):
            while st and arr[st[-1]] > arr[i]:
                prevSmaller[st.pop()] = i
            st.append(i)
        
        res = 0
        for i in range(len(arr)):
            res += (nextSmaller[i] - i) * (i - prevSmaller[i]) * arr[i]
            res = res % (10 ** 9 + 7)
        
        return res