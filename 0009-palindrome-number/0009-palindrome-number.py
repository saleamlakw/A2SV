class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversed = 0
        temp = x
        if x<0:
            return False
        while temp:
            reversed *= 10
            reversed += (temp%10)
            temp//=10

        return reversed == x