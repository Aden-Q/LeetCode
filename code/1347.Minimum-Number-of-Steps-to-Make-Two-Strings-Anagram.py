from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # First of all, s and t must be of the same length
        # in order to make them anagram
        # Second, if they are of the same length, there is always
        # a way to make them anagram
        # Lastly, we can use a dictionary to count the frequency of each
        # distinct character in our source string s, compare its frequency with the one in t
        # If we have s: d1[c] < t: d2[c], then we may replace num = d2[c] - d1[c] so many characters
        # The replacement we choose must satisfy: d2[c'] > d2[c'] to minimize the steps
        
        counter1 = Counter(s)
        counter2 = Counter(t)
        ans = 0
        
        for key in counter1.keys():
            if counter1[key] > counter2[key]:
                ans += counter1[key] - counter2[key]
        
        return ans