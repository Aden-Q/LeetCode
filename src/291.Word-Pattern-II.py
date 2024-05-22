class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        table = {}

        def feasible(table, reverse_table, idx_pattern, idx_s) -> bool:
            if idx_pattern == len(pattern) and idx_s == len(s):
                return True
            
            if idx_pattern == len(pattern) or idx_s == len(s):
                return False

            # use an existing mapping
            if pattern[idx_pattern] in table:
                mapped_word = table[pattern[idx_pattern]]
                if not s[idx_s:].startswith(mapped_word):
                    return False
                
                return feasible(table, reverse_table, idx_pattern+1, idx_s + len(mapped_word))

            # we need a new mapping, brute force for all possibilities
            for next_idx in range(idx_s+1, len(s) + 1):
                mappeed_word = s[idx_s:next_idx]
                if mappeed_word in reverse_table:
                    continue

                table[pattern[idx_pattern]] = mappeed_word
                reverse_table[mappeed_word] = pattern[idx_pattern]
                if feasible(table, reverse_table, idx_pattern+1, next_idx):
                    return True

                # backtrack
                del table[pattern[idx_pattern]]
                del reverse_table[mappeed_word]

            return False

        return feasible({}, {}, 0, 0)    
