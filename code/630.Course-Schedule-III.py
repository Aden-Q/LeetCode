class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # we use a map heap to store the duration of courses that have been taken so far
        # every time if we've seen a new course
        # if the current course canbe taken (current_timestamp + duration <= end_time)
        # we simply take this course and update the current_timestamp
        # otherwise we eject a previously taken course that has the maximum duration
        # and replace it with the current course, so that we have a smaller "current_timetamp"
        # providing more space to take other courses
        # first we need to sort all courses by their endtime
        courses.sort(key=lambda x: x[1])
        max_hq = []
        curr_time = 0
        for duration, end_time in courses:
            if curr_time + duration <= end_time:
                heapq.heappush(max_hq, -duration)
                curr_time += duration
            elif max_hq and -max_hq[0] > duration:
                # only in this case we can greedily take a new course and reduce the current timestamp
                # eject a previous course with the longest duration
                curr_time -= - heapq.heappop(max_hq)
                # inject a new course and reduce the current timestamp
                curr_time += duration
                heapq.heappush(max_hq, -duration)

        return len(max_hq)
