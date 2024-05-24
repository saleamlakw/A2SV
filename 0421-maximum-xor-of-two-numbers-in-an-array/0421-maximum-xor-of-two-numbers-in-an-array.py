class TrieNode:
    def __init__(self):
        self.children={}
        self.isEnd=False
class Trie:
    def __init__(self):
        self.root=TrieNode()
    def insert(self,word):
        cur=self.root
        for letter in word:
            if letter not in cur.children:
                 cur.children[letter]=TrieNode() 
            cur=cur.children.get(letter)
        cur.isEnd=True
    def search(self,word):
        cur=self.root
        for letter in word:
            if letter not in cur.children:
                return False
            cur=cur.children[letter]
        return cur.isEnd
    def startWith(self,prefix):
        cur=self.root
        for letter in prefix:
            if letter not in cur.children:
                return False
            cur=cur.children.get(letter)
        return True
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie=Trie()
        n=(max(nums).bit_length())
        print(n)
        for ele in nums:
            b=bin(ele)[2:]
            bi="0"*(n-len(b))+b
            trie.insert(bi)
        result=0
        for num in nums:
            re=0
            cur=trie.root.children
            for i in range(n-1,-1,-1):
                if (num & 1<<i):
                    if "0" in cur:
                        re=re|1<<i
                        cur=cur["0"].children
                    else:
                        cur=cur["1"].children
                else:
                    if "1" in cur:
                        re=re|1<<i
                        cur=cur["1"].children
                    else:
                        cur=cur["0"].children
              
            result=max(result,re)
        return result

        