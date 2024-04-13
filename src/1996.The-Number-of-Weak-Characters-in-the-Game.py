class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        # Sort the characters by their start time
        properties.sort(key = lambda x : (x[0], -x[1]))
        st = []
        nextLargerDefense = [-1] * len(properties)
        
        for idx, val in enumerate(properties):
            attack, defense = val
            while st and properties[st[-1]][1] < defense:
                nextLargerDefense[st.pop()] = idx
            st.append(idx)
        
        cnt = 0
        for i in range(len(properties)):
            if nextLargerDefense[i] == -1:
                continue
            cnt += 1
        return cnt