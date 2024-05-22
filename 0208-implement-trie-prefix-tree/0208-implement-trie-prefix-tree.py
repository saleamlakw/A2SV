class TrieNode:
    def __init__(self):
        self.children=[ None for _ in range(26) ]
        self.isEnd=False
class Trie:
    def __init__(self):
        self.root=TrieNode()
    def insert(self, word: str) -> None:
        cur=self.root
        for letter in word:
            ind=ord(letter)-ord('a')
            if not cur.children[ind]:
                cur.children[ind]=TrieNode()
            cur=cur.children[ind]
        cur.isEnd=True
        
    def search(self, word: str) -> bool:
        
        cur=self.root
        for letter in word:
            ind=ord(letter)-ord('a')
            cur = cur.children[ind]
            if not cur :
                return False
        return cur.isEnd

    def startsWith(self, prefix: str) -> bool:
        cur=self.root
        for letter in prefix:
            ind=ord(letter)-ord('a')
            cur = cur.children[ind]
            if not cur :
                return False
        return True
      
       
      


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)