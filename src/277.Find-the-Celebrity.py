# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        # n^2 solution is easy: check for every pair and returns the node with in_degree=n-1 and out_degree=0
        candidate_indices = set([i for i in range(n)])

        while len(candidate_indices) > 1:
            candidate_list = list(candidate_indices)
            first, second = random.choice(candidate_list), random.choice(candidate_list)
            while second == first:
                second = random.choice(candidate_list)

            if knows(first, second):
                # the first person knows the second person, then the first person cannot be the celebriity
                candidate_indices.remove(first)
            else:
                # the first person does not know the second person, then the second person cannot be the celebrity
                candidate_indices.remove(second)

        # so far we've made n-1 calls to the API knows, and we only have 1 candidate left
        # we need to do two more checks:
        # 1. whether this person does not know any other person
        # 2. whether all other people know this person
        candidate = candidate_indices.pop()
        for i in range(n):
            if i == candidate:
                continue
            if knows(candidate, i):
                return -1
            if not knows(i, candidate):
                return -1

        return candidate
