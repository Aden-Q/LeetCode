class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        bucketSize = valueDiff + 1
        buckets = defaultdict(int)
        # bucket size: valueDiff + 1 [0, valueDiff], [valueDiff + 1, 2 * valueDiff + 1], etc

        def getBucketID(x):
            nonlocal bucketSize
            return x // bucketSize if x >= 0 else (x - 1) // bucketSize

        for i in range(min(indexDiff + 1, len(nums))):
            bucket_idx = getBucketID(nums[i])
            # check the current bucket and neighbor buckets
            if bucket_idx in buckets:
                return True
            # check neighbor buckets
            if bucket_idx - 1 in buckets and nums[i] - buckets[bucket_idx - 1] <= valueDiff:
                return True
            if bucket_idx + 1 in buckets and buckets[bucket_idx + 1] - nums[i] <= valueDiff:
                return True

            buckets[bucket_idx] = nums[i]

        for i in range(indexDiff + 1, len(nums)):
            # remove a previous element
            bucket_idx_prev = getBucketID(nums[i - indexDiff - 1])
            del buckets[bucket_idx_prev]

            # add a new element
            bucket_idx_curr = getBucketID(nums[i])
            # check the current bucket and neighbor buckets
            if bucket_idx_curr in buckets:
                return True
            # check neighbor buckets
            if bucket_idx_curr - 1 in buckets and nums[i] - buckets[bucket_idx_curr - 1] <= valueDiff:
                return True
            if bucket_idx_curr + 1 in buckets and buckets[bucket_idx_curr + 1] - nums[i] <= valueDiff:
                return True

            buckets[bucket_idx_curr] = nums[i]

        return False
