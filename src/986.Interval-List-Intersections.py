class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        first_ptr, second_ptr = 0, 0
        ans = []

        while first_ptr < len(firstList) and second_ptr < len(secondList):
            first_start, first_end = firstList[first_ptr][0], firstList[first_ptr][1]
            second_start, second_end = secondList[second_ptr][0], secondList[second_ptr][1]

            if first_end < second_start:
                first_ptr += 1
            elif first_start > second_end:
                second_ptr += 1
            else:
                # there's an overlap
                ans.append([max(first_start, second_start), min(first_end, second_end)])

                if first_end > second_end:
                    second_ptr += 1
                else:
                    first_ptr += 1

        return ans
