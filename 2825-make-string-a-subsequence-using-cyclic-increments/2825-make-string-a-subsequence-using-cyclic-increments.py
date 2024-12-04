class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        def change(char):
            asci = ((ord(char)  - (ord("a")-1))) % 26
            return chr(asci+ord("a"))

        left = 0
        right = 0

        while left < len(str1) and right < len(str2):
            if str1[left] == str2[right] or change(str1[left]) == str2[right]:
                left += 1
                right += 1
            else:
                left += 1
        return right == len(str2)
         