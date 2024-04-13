class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev_num_devices = 0
        curr_num_devices = 0
        ans = 0
        for i in range(len(bank)):
            row = bank[i]
            # we need to count the number of laser beams on the current row
            for j in range(len(row)):
                if row[j] == '1':
                    curr_num_devices += 1
            if curr_num_devices == 0:
                continue
            ans += prev_num_devices * curr_num_devices
            prev_num_devices = curr_num_devices
            curr_num_devices = 0

        return ans
