class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        envelopes.sort(key = lambda x: (x[0], -x[1]))
        ends = [x[1] for x in envelopes]
        sub_seq = [ends[0]]
        for end in ends:
            idx = bisect_left(sub_seq, end)
            if idx == len(sub_seq):
                sub_seq.append(end)
            else:
                sub_seq[idx] = end

        return len(sub_seq)   
