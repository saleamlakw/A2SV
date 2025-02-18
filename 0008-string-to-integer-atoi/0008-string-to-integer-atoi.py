class Solution(object):
    def myAtoi(self, s):
        #when s is empty return 0
        if not s:
            return 0
        #check the sign of the string 
        #we have to skip all empty spaces and leading zeros 
        start = 0
        while start < len(s) and s[start] ==" ":
            start += 1
        sign = 1
        if start < len(s):
            if s[start]=="-":
                sign = -1
                start += 1
            elif s[start]=="+":
                sign = 1
                start += 1
        while start < len(s) and s[start]==0:
            start += 1
        # print(start)
        #iterate through the string and extract all the numbers 
        num = 0
        for char in s[start:]:
            if not char.isnumeric():
                break
            else:
                num *= 10
                num += int(char)
        #check wheather the number inbound(>-2**31 and < 2**31 - 1)
        num *= sign
        if num < -1*(1<<31):
            return -1*(1<<31)
        elif num > (1<<31)-1:
            return (1<<31)-1
        else:
            return num
        #return ans
        