class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        count_ones = sum(students)
        count_zeros = len(students) - count_ones
        students = deque(students)
        sandwiches = deque(sandwiches)
        while students:
            if sandwiches[0] == 1 and count_ones == 0:
                break
            if sandwiches[0] == 0 and count_zeros == 0:
                break

            if students[0] != sandwiches[0]:
                students.append(students.popleft())
                continue
            
            if students[0] == sandwiches[0] == 0:
                count_zeros -= 1
            else:
                count_ones -= 1

            students.popleft()
            sandwiches.popleft()

        return len(students)
