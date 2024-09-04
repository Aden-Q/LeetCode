class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # convert it to a hashmap for fast O(1) lookup
        obstacles = set((p[0], p[1]) for p in obstacles)

        # direction vectors
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        # direction index
        d_idx = 0
        pos = [0, 0]
        max_eu_dist = 0

        for command in commands:
            # deal with turn commands first
            if command == -1:
                # turn right
                d_idx = (d_idx + 1) % 4
            elif command == -2:
                # turn left
                d_idx = (d_idx - 1) % 4
            else:
                # otherwise go ahead and check for obstacles
                # given that the integer is only in range [1, 9]
                # it's safe to do as an iteration
                # unwrap
                dx, dy = directions[d_idx]
                px, py = pos
                while command:
                    # one step at a time
                    command -= 1
                    if (px + dx, py + dy) in obstacles:
                        break
                    else:
                        px += dx
                        py += dy

                pos = [px, py]

                max_eu_dist = max(max_eu_dist, px**2 + py**2)

        return max_eu_dist
