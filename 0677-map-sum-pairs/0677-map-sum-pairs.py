class TrieNode:
    def __init__(self):
        self.children={}
        self.isEnd=False
        self.fre=0
        
class Trie:
    def __init__(self):
        self.root=TrieNode()
        self.pre={}
    def insert(self,word,val):
        cur=self.root
        if word in self.pre:
             for letter in word:
                cur=cur.children[letter]
                cur.fre-=self.pre[word]
        cur=self.root
        for letter in word:
            if letter not in cur.children:
                cur.children[letter]=TrieNode()
            cur=cur.children[letter]
            cur.fre+=val
        cur.isEnd=True
        self.pre[word]=val
    def search(self,word):
        cur=self.root
        for letter in word:
            if letter not in  cur.children:
                return 0
            cur=cur.children[letter]
        return cur.fre
class MapSum:

    def __init__(self):
        self.trie=Trie()

    def insert(self, key: str, val: int) -> None:
        self.trie.insert(key,val)

    def sum(self, prefix: str) -> int:
        return self.trie.search(prefix)


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)