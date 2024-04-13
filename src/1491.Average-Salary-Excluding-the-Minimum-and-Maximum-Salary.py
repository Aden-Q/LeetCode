class Solution:
    def average(self, salary: List[int]) -> float:
        n = len(salary)
        running_sum = 0
        min_salary = float('inf')
        max_salary = 999
        for s in salary:
            running_sum += s
            min_salary = min(min_salary, s)
            max_salary = max(max_salary, s)
        return (running_sum - min_salary - max_salary) / (n - 2)