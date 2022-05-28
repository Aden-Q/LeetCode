from collections import defaultdict
class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        dc = defaultdict(int)
        max_cnt = 0
        cand_list = []
        for i in range(len(senders)):
            dc[senders[i]] += len(messages[i].split())
            if dc[senders[i]] == max_cnt:
                cand_list.append(senders[i])
            elif dc[senders[i]] > max_cnt:
                cand_list.clear()
                cand_list.append(senders[i])
                max_cnt = dc[senders[i]]
        return max(cand_list)