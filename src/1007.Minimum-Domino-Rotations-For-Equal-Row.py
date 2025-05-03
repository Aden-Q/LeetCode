class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        counter_top = Counter()
        counter_bottom = Counter()
        counter_dups = Counter()
        length = len(tops)

        for idx in range(length):
            top = tops[idx]
            bottom = bottoms[idx]
            counter_top[top] += 1
            counter_bottom[bottom] += 1

            if top == bottom:
                counter_dups[top] += 1

        min_steps = inf
        for key in counter_top:
            if counter_top[key] + counter_bottom[key] - counter_dups[key] == length:
                min_steps = min(min_steps, min(counter_top[key], counter_bottom[key]) - counter_dups[key])
        
        return min_steps if min_steps != inf else -1
