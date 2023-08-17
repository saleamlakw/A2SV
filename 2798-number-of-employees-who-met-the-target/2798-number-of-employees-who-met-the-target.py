class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        re=0
        for i in hours:
            if i>=target:
                re+=1
        return re
        