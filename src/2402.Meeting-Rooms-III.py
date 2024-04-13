class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # count the number of times each room is used
        counts = [0] * n
        # based on rule 3, we sort the meetings by their starting time
        meetings.sort()
        # keep track of which rooms is free to use
        unused_rooms = [idx for idx in range(n)]
        heapq.heapify(unused_rooms)
        # O(log n) to get the first unused room
        def getFirstUnused(unused_rooms):
            return heapq.heappop(unused_rooms) if unused_rooms else -1

        # we process meetings in order, by their start time. For some meeting
        # 1. If there's some empty room left, we schedule the meeting in that room
        # 2. If there's no empty room left, we delay the meeting until the meeting with the earliest end time ends, and schedule the current meeting in that room
        # a priority queue to keep track of meetings's end time that are currently scheduled
        pq = []
        for start_time, end_time in meetings:
            if pq and pq[0][0] <= start_time:
                while pq and pq[0][0] <= start_time:
                    # remove those meetings that have end
                    _, prev_meeting_room_idx = heapq.heappop(pq)
                    heapq.heappush(unused_rooms, prev_meeting_room_idx)

            unused_room_idx = getFirstUnused(unused_rooms)
            if unused_room_idx != -1:
                # we have a free room to schedule the meeting
                counts[unused_room_idx] += 1
                # push end time of the meeting and the room index into the priority queue
                heapq.heappush(pq, [end_time, unused_room_idx])
            else:
                # in this case we have to delay the current meeting because no rooms are available to schedule the current meeting
                prev_meeting_end_time, prev_meeting_room_idx = heapq.heappop(pq)
                # delay the current meeting
                end_time = end_time + prev_meeting_end_time - start_time
                # this room is used again
                counts[prev_meeting_room_idx] += 1
                heapq.heappush(pq, [end_time, prev_meeting_room_idx])

        return counts.index(max(counts))
