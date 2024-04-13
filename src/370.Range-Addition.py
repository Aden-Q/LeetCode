class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        # typical differential array problem
        # diff[i] = arr[i] - arr[i-1]
        diff = [0] * length
        arr = [0] * length
        
        for update in updates:
            startIdx, endIdx, inc = update
            diff[startIdx] += inc
            if endIdx + 1 < length:
                diff[endIdx + 1] -= inc
                
        arr[0] = diff[0]
        for i in range(1, length):
            arr[i] = arr[i-1] + diff[i]
        
        return arr