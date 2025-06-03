class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        n = len(status)

        # starting from the given boxes (it needs to be a set because we may find some keys to them later on the visiting path), calculate how many candies we can get in total
        # we use the keys array to mutate the status array: once we find some key, change the status from 0 (closed) to 1 (open)
        def dfs(boxes: set) -> int:
            nonlocal status, candies, keys, containedBoxes
            to_be_removed = []
            to_be_added = []

            ans = 0
            for box in boxes:
                if status[box] == 1:
                    # we find a box we can open
                    to_be_added.extend(containedBoxes[box])
                    to_be_removed.append(box)
                    for key in keys[box]:
                        # open those boxes so we can explore them further
                        status[key] = 1
                    ans += candies[box]
            
            for box in to_be_removed:
                boxes.discard(box)
            
            for box in to_be_added:
                boxes.add(box)
            
            if ans == 0:
                return 0
            
            return ans + dfs(boxes)

        return dfs(set(initialBoxes))
            class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        n = len(status)

        # starting from the given boxes (it needs to be a set because we may find some keys to them later on the visiting path), calculate how many candies we can get in total
        # we use the keys array to mutate the status array: once we find some key, change the status from 0 (closed) to 1 (open)
        def dfs(boxes: set) -> int:
            nonlocal status, candies, keys, containedBoxes
            to_be_removed = []
            to_be_added = []

            ans = 0
            for box in boxes:
                if status[box] == 1:
                    # we find a box we can open
                    to_be_added.extend(containedBoxes[box])
                    to_be_removed.append(box)
                    for key in keys[box]:
                        # open those boxes so we can explore them further
                        status[key] = 1
                    ans += candies[box]
            
            for box in to_be_removed:
                boxes.discard(box)
            
            for box in to_be_added:
                boxes.add(box)
            
            if ans == 0:
                return 0
            
            return ans + dfs(boxes)

        return dfs(set(initialBoxes))
