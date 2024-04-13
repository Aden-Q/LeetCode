class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # for every num nums[j], we search from index 0...j, to find the maximum index i such that nums[j], nums[i] has a distance smaller than t, we also search for the distance t such that it's the kth smallest distance among all pairs
        nums.sort()
        # [dist_left, dist_right)
        dist_left, dist_right = 0, nums[-1] - nums[0] + 1
        
        while dist_left < dist_right:
            dist = (dist_right - dist_left) // 2 + dist_left
            # for dist, we need to find the number of pairs such that those pairs have a dist smaller or equal to this
            num_pairs = 0
            for j in range(1, len(nums)):
                i_left, i_right = 0, j
                while i_left < i_right:
                    i_mid = (i_right - i_left) // 2 + i_left
                    if nums[j] - nums[i_mid] <= dist:
                        # we can find more pairs
                        i_right = i_mid
                    else:
                        i_left = i_mid + 1
                
                num_pairs += j - i_left
            
            # there are num_pairs of such pairs that have a distance <= dist
            if num_pairs >= k:
                # too many pairs, we need to reduce the dist
                dist_right = dist
            else:
                dist_left = dist + 1

        return dist_left
