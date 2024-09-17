class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ind=float("inf")

        for i,char in enumerate(word):
            if char == ch:
                ind = min (ind,i)

        if ind == float("inf"):
            return word
        else:
            return word[:ind+1][::-1]+word[ind+1:]

