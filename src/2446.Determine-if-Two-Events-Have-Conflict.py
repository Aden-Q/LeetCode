class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        def time_to_minutes(time_hm) -> int:
            hour, minute = time_hm.split(':')
            return int(hour) * 60 + int(minute)

        start1, end1 = time_to_minutes(event1[0]), time_to_minutes(event1[1])
        start2, end2 = time_to_minutes(event2[0]), time_to_minutes(event2[1])

        if start1 > start2:
            start1, end1, start2, end2 = start2, end2, start1, end1
        
        return end1 >= start2