class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def isValid(counter1, counter2):
            for k, v in counter.items():
                if k not in counter1.keys() or v > counter1[k]:
                    return False
            return True
        counter = {}
        window_counter = {}
        for c in t:
            if c not in counter.keys():
                counter[c] = 1
            else:
                counter[c] += 1
        left = 0
        min_string = s + '.'
        right = -1
        while right < len(s):
            # if debug == True:
            #     print(left, ' ', right, ' ', window_counter)
            if isValid(window_counter, counter):
                if right - left + 1 < len(min_string):
                    min_string = s[left:right+1]
                window_counter[s[left]] -= 1
                left += 1
            else:
                right += 1
                if right >= len(s):
                    break
                if s[right] not in window_counter.keys():
                    window_counter[s[right]] = 1
                else:
                    window_counter[s[right]] += 1
                
        if len(min_string) == len(s) + 1:
            return ""
        else:
            return min_string