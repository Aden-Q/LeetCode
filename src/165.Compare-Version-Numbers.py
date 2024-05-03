class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        revisions1 = version1.split('.')
        revisions1 = [int(val) for val in revisions1]
        revisions2 = version2.split('.')
        revisions2 = [int(val) for val in revisions2]
        
        idx = 0
        while idx < len(revisions1) and idx < len(revisions2):
            if revisions1[idx] < revisions2[idx]:
                return -1
            elif revisions1[idx] > revisions2[idx]:
                return 1
            idx += 1

        while idx < len(revisions1):
            if revisions1[idx] > 0:
                return 1
            idx += 1

        while idx < len(revisions2):
            if revisions2[idx] > 0:
                return -1
            idx += 1

        return 0
