class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        idx = 0
        
        while idx < len(data):
            curr = format(data[idx], '08b')[-8:]
            if curr[0] == '0':
                # Is a one-byte character
                idx += 1
            else:
                # Check number of bytes
                numBytes = 0
                start = 0
                while start < 8 and curr[start] != '0':
                    numBytes += 1
                    start += 1
                if numBytes == 1 or numBytes > 4:
                    # Only allow 1-4 bytes long
                    return False
                # Otherwise check whether the next numBytes - 1 bytes are valid
                idx += 1
                for _ in range(numBytes - 1):
                    if idx >= len(data) or format(data[idx], '08b')[-8:][:2] != '10':
                        return False
                    idx += 1
        
        return True