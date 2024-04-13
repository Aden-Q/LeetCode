class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        max_freq = max(counter.values())

        buckets = [[] for _ in range(max_freq + 1)]
        for key, val in counter.items():
            buckets[val].append(key)

        # build the string by iterating backwards from the bucket
        res = []
        for i in range(max_freq, 0, -1):
            for key in buckets[i]:
                res.append(key * i)

        return ''.join(res)
