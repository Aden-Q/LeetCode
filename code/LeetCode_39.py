class Solution:
    def concatenate_list(self, list1, list2):
        res = []
        if not list1 and list2:
            return list2
        if list1 and not list2:
            return [list1]
        for l2 in list2:
            list_temp = list1.copy()
            list_temp.extend(l2)
            res.append(list_temp)
        return res
    
    def recursive_combine(self, candidates, target):
        # two special cases
        if len(candidates) == 0:
            return []
        if len(candidates) == 1 and target != 0:
            if target % candidates[0] == 0:
                times = target // candidates[0]
                return [[candidates[0]] * times]
            else:
                return []

        counter = 0
        res = []
        while counter * candidates[0] <= target:
            first_list = [candidates[0]] * counter
            second_list = self.recursive_combine(candidates[1:], target - candidates[0] * counter)
            if second_list or counter * candidates[0] == target:
                temp_res = self.concatenate_list(first_list, second_list)
                # print(first_list, ' ', second_list, ' ', counter, ' ', temp_res)
                res.extend(temp_res)
            counter += 1
        return res

    def combinationSum(self, candidates, target: int):
        return self.recursive_combine(candidates, target)

if __name__ == '__main__':
    test = Solution()
    candidates = [2, 3]
    target = 7
    res = test.combinationSum(candidates, target)
    print(res)