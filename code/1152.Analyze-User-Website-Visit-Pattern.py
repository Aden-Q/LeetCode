from collections import defaultdict
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        # Maintain a mapping from each user to the websites they visited in timestamp ordering (for each user)
        ht = defaultdict(list)
        length = len(username)
        for i in range(length):
            ht[username[i]].append((website[i], timestamp[i]))
            
        for user in ht.keys():
            ht[user].sort(key = lambda x : x[1])
            
        # Enumerate all visit patterns (for each user)
        # a pattern is a subsequence of length 3
        freq = defaultdict(int)
        for user in ht.keys():
            num_websites = len(ht[user])
            # A hashset to keep track of all visiter patterns
            hashset = set()
            for i in range(num_websites):
                for j in range(i+1, num_websites):
                    for k in range(j+1, num_websites):
                        # Check whether the current pattern has been recorded
                        # If not, add it to the hashset
                        curr_pattern = '%s %s %s' % (ht[user][i][0], ht[user][j][0], ht[user][k][0])
                        if curr_pattern not in hashset:
                            freq[curr_pattern] += 1
                            hashset.add(curr_pattern)
        
        # Get the pattern corresponding to the max value in freq
        res = []
        max_cnt = max(freq.values())
        for key in freq.keys():
            if freq[key] == max_cnt:
                res.append(key.split())
        
        return min(res)