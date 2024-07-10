class Solution:
    def minOperations(self, logs: List[str]) -> int:
        # keep track of the depth of the current dir
        level = 0
        for log in logs:
            if log == "../":
                level = max(0, level - 1)
            elif log == "./":
                continue
            else:
                level += 1

        return level
