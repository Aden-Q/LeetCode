class Solution:
    def minAvailableDuration(
        self, slots1: List[List[int]], slots2: List[List[int]], duration: int
    ) -> List[int]:
        # sort and greedy
        # sort by start time so that we can find the earliest time slot using a greedy algorithm
        slots1.sort(key=lambda x: x[0])
        slots2.sort(key=lambda x: x[0])

        # indices into the slots
        idx1, idx2 = 0, 0
        while idx1 < len(slots1) and idx2 < len(slots2):
            s1, s2 = slots1[idx1], slots2[idx2]
            s1_start, s1_end = s1
            s2_start, s2_end = s2
            # check whether the current slot has enough time to cover the duration, for person 1
            if s1_start + duration > s1_end:
                idx1 += 1
                continue
            # check whether the current slot has enough time to cover the duration, for person 2
            if s2_start + duration > s2_end:
                idx2 += 1
                continue
            # check intersection between 2 people
            # if s1 comes too early, we need the next s1
            # s1_start ----- s1_end
            # -----------s2_start ------s2_end
            if s2_start + duration > s1_end:
                idx1 += 1
                continue
            # the other case
            if s1_start + duration > s2_end:
                idx2 += 1
                continue
            # otherwise there's an intersation to satify the requirement
            start_time = max(s1_start, s2_start)

            return [start_time, start_time + duration]

        # cannot find any slot, then return an empty array
        return []
