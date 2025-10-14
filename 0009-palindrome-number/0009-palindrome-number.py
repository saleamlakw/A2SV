class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversed = 0
        temp = x
        if x<0:
            return False
        while temp:
            reversed += (temp%10)
            temp//=10
            if temp : reversed *= 10
        print(reversed)
        return reversed == x