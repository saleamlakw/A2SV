class Solution:
    def smallestPalindrome(self, s: str) -> str:
        count = Counter(s)
        mid = ""
        ans = ""
        for ele in sorted(set(s)):
            if count[ele] % 2 :
                mid = ele
            ans += (count[ele]//2)*ele
        return ans + mid + ans[::-1]
