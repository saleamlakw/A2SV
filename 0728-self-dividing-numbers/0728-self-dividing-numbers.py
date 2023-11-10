class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def check(num):
            for n in str(num):
                if "0" in n: 
                    return False
                if num%int(n)!=0:
                    return False
            return True
        result=[]
        for i in range(left,right+1):
            if check(i):
                result.append(i)
        return result
