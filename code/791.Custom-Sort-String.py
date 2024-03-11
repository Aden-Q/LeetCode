class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order_dict = dict((val, idx) for idx, val in enumerate(order))
        s_list = list(s)
        s_list.sort(key = lambda x: order_dict[x] if x in order_dict else 0)
        return ''.join(s_list)
