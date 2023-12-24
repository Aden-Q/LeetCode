class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        # index of the first group
        idx = 0
        # the index to overwrite
        write_idx = 0

        while idx < n:
            group_len = 1
            while idx + group_len < n and chars[idx + group_len] == chars[idx]:
                group_len += 1
            chars[write_idx] = chars[idx]
            write_idx += 1
            # write the count if group_len > 1
            if group_len > 1:
                group_len_str = str(group_len)
                str_len = len(group_len_str)
                chars[write_idx:write_idx + str_len] = [c for c in group_len_str]
                write_idx += str_len

            idx += group_len

        return write_idx
