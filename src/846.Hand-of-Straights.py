class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counter = Counter(hand)
        heapq.heapify(hand)

        while hand:
            top = heapq.heappop(hand)
            if counter[top] == 0:
                continue

            # otherwise we try to form a group of the give size
            counter[top] -= 1

            # we need top, top + 1, top + groupSize - 1 to form a group of size groupSize
            for diff in range(1, groupSize):
                next_card = top + diff
                if counter[next_card] <= 0:
                    # not feasible so return false immediately
                    return False
                
                counter[next_card] -= 1
        
        return True
