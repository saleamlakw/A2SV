class Solution(object):
    def countHomogenous(self, s):
        window=deque()
        result=0
        l=0
        for i,r in enumerate(s):
            window.append(r)
            while window and window[0]!=r:
                window.popleft()
            l,r=0,len(window)
            if len(window)>1:
                        result+=len(window)-2
            if len(window)>1:
                    result+=1
        return (result+len(s))%(10**9+7)
# window=[a,a]
# co={a:2,b:1,bb:1,c:1,cc:1,ccc:1,aa:1}
#counter to keep track of frequency of each homogenous substrings 
#sliding window to get the homogenous substrings 
