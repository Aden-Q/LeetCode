class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        # For each range, since the notation is "a->b" or "a", we need to find its left bound and right bound
        start, end = lower, lower
        res = []
        
        for num in nums:
            if num == start:
                start += 1
                continue
            
            # Now we have num != start, then we must have num > start
            # Find the right bound
            end = num - 1
            if start == end:
                res.append("%d" % start)
            else:
                res.append("%d->%d" % (start, end))
            
            # Update start point to find the next interval
            start = num + 1
        
        if start == upper:
            res.append("%d" % start)
        elif start < upper:
            res.append("%d->%d" % (start, upper))
        
        return res