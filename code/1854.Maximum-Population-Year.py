class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        # Year_Converted = Year - 1949
        # The converted year is between 1 and 101
        diff_array = [0] * 102
        
        for log in logs:
            birth_converted = log[0] - 1949
            die_converted = log[1] - 1949
            # Add one to those year between birth_converted
            # and die_converted - 1, inclusive
            diff_array[birth_converted] += 1
            diff_array[die_converted] -= 1
            
        curr_pop = 0
        max_pop = 0
        earliest_year = 0
        for i in range(1, 101):
            curr_pop += diff_array[i]
            if curr_pop > max_pop:
                max_pop = curr_pop
                earliest_year = i + 1949
        
        return earliest_year