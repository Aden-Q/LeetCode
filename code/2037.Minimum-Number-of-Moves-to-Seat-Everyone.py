class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        res = sum([abs(seats[i] - students[i]) for i in range(len(students))])
        return res