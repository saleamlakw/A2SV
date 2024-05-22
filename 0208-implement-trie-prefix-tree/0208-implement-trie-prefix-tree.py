class TrieNode:
    def __init__(self):
        self.childrens=defaultdict(TrieNode)
        self.isEnd=False
class Trie:

    def __init__(self):
        self.root=TrieNode()
    def insert(self, word: str) -> None:
        current=self.root
        for letter in word:
            current=current.childrens[letter]
        current.isEnd=True
        

    def search(self, word: str) -> bool:
        current=self.root
        for letter in word:
            current=current.childrens[letter]
            if not current:
                return False
           
        return current.isEnd

    def startsWith(self, prefix: str) -> bool:
        current=self.root
        for letter in prefix:
            current=current.childrens.get(letter)
            if not current:
                return False
       
        return True and current.childrens


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)