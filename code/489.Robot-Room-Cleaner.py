# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        # initially the robot faces up
        init_pos = (0, 0)
        init_dir = (-1, 0)
        turn_left = {
            (-1, 0): (0, -1),
            (0, -1): (1, 0),
            (1, 0): (0, 1),
            (0, 1): (-1, 0),
        }
        turn_right = {
            (-1, 0): (0, 1),
            (0, 1): (1, 0),
            (1, 0): (0, -1),
            (0, -1): (-1, 0),
        }
        visited = set()

        # run dfs from the current position to clean the room
        def dfs(curr_pos, curr_dir):
            print(curr_pos, curr_dir)
            if curr_pos in visited:
                return
            # otherwise we clean the current slot
            visited.add(curr_pos)
            robot.clean()

            # visit all neighbors
            # turn left
            # we can make 1~3 number of turns
            for turn_cnt in range(4):   
                robot.turnLeft()
                next_dir = turn_left[curr_dir]
                curr_dir = next_dir
                # check if we can move in the current direction
                if robot.move():
                    next_pos = (curr_pos[0] + next_dir[0], curr_pos[1] + next_dir[1])
                    dfs(next_pos, next_dir)
                    # backtrack, we need to move back to the original position and restore the direction
                    for _ in range(2):
                        robot.turnRight()
                        next_dir = turn_right[next_dir]
                    # move back
                    robot.move()
                    while next_dir != curr_dir:
                        robot.turnRight()
                        next_dir = turn_right[next_dir]

            return

        dfs(init_pos, init_dir)