class Solution:
    def average(self, salary: List[int]) -> float:
        tot= (sum(salary)-(min(salary)+max(salary)))
        return tot/(len(salary)-2)