class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits=list(map(lambda x:str(x),digits))
        re="".join(digits)
        re=int(re)+1
        return [int(i) for i in str(re)]
        