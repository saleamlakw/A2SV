class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        re=0
        for i in operations:
            if "-" in i:
                re-=1
            if "+" in i:
                re+=1
        return re
        