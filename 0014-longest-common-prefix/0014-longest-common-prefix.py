class TrieNode:
    def __init__(self):
        self.childrens=defaultdict(TrieNode)
        self.isEnd=False

class Trie:
    def __init__(self):
        self.root=TrieNode()

    def insert(self,word):
        current=self.root
        for letter in word:
            current=current.childrens[letter]
        current.isEnd=True
    def search(self,word):
        current=self.root
        for letter in word:
            current=current.childrens.get(letter)
            if not current:
                return False 
        return current.isEnd
    def startsWith(self,prefix):
        current=self.root
        for letter in word:
            current=current.childrens.get(letter)
            if not current:
                return False
        return True
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
            trie=Trie()
            result=""
            for ele in strs:
                trie.insert(ele)
            
            key=strs[0]
            cur=trie.root.childrens
            # print(cur)
            if len(cur)!=1:
                return ""     
            for letter in key:
                result+=letter
                cur=cur[letter].childrens
                if len(cur)!=1:
                    break
                
            return result
                    
                
