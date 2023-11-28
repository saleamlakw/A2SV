class Solution(object):
    def reversePrefix(self, word, ch):
        switch=True
        result=""
        for i in range(len(word)):
            result+=word[i]
            if word[i]==ch and switch:
                switch=False
                result=result[::-1]
        return result
        