class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
    
        pre=Counter(words[0])
        cur=Counter()

        for j in range(1,len(words)):
            count=Counter(words[j])
            for letter in count:
                if letter in pre:
                    cur[letter]=min(count[letter],pre[letter])
            pre=cur
            cur=Counter()
        
        result=[]
        for chr in pre:
            result.extend([chr]*pre[chr])
        return result

